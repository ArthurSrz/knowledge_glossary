#!/usr/bin/env python3
"""Formal reasoning over the knowledge glossary using Datalog."""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

GRAPH_DIR = Path("graph")
STATS_DIR = Path("stats")
REPORT_FILE = STATS_DIR / "reasoning_report.md"

RELATION_MAP = {
    "broader": "broader",
    "skos:broader": "broader",
    "subclass of": "broader",
    "skos:narrower": "narrower",
    "skos:related": "related",
    "related_to": "related",
    "oppositeOf": "opposite_of",
    "uses": "uses",
    "dependencies": "depends_on",
    "studied in": "studied_in",
    "CanBeConstructedWith": "constructed_with",
    "contributing factor of": "contributing_factor",
    "has use": "has_use",
}

# ── SKOS rule set ─────────────────────────────────────────────────────
# TODO: Write your Datalog rules here (~9 lines).
#
# Each rule is a string in Datalog syntax: "head(X,Y) :- body1(X,Z), body2(Z,Y)"
# Variables are uppercase (X, Y, Z). Constants are lowercase atoms.
#
# Intended semantics to encode:
#   1-2. ancestor(X,Y) = transitive closure of broader (base case + recursive)
#   3-4. broader and narrower are inverses (derive each from the other)
#   5-6. related_s(X,Y) = symmetric closure of related
#   7.   in_cycle(X) = X is its own ancestor (consistency violation)
#   8.   conflict(X,Y) = related_s AND opposite_of between X,Y (consistency)
#   9.   s27_violation(X,Y) = related_s AND ancestor between X,Y (SKOS S27:
#        skos:related is disjoint with the hierarchical relation)
#
SKOS_RULES = [
    "ancestor(X, Y) :- broader(X, Y)",
    "ancestor(X, Y) :- broader(X, Z), ancestor(Z, Y)",
    "broader(X, Y) :- narrower(Y, X)",
    "narrower(X, Y) :- broader(Y, X)",
    "related_s(X, Y) :- related(X, Y)",
    "related_s(X, Y) :- related(Y, X)",
    "in_cycle(X) :- ancestor(X, X)",
    "conflict(X, Y) :- related_s(X, Y), opposite_of(X, Y)",
    "s27_violation(X, Y) :- related_s(X, Y), ancestor(X, Y)",
]
# ──────────────────────────────────────────────────────────────────────


def slugify(name):
    s = unicodedata.normalize("NFKD", name)
    s = s.encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return f"c_{s}" if s else "c_unnamed"


def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def parse_targets(value):
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    targets = []
    for v in value:
        if not isinstance(v, str):
            continue
        for m in re.finditer(r"\[\[([^\]|#]+)\]\]", v):
            t = m.group(1)
            t = re.sub(r"^graph/", "", t)
            t = re.sub(r"\.md$", "", t)
            targets.append(t.strip())
    return targets


def load_notes(graph_dir):
    notes = {}
    filenames = {}
    parse_errors = []
    unmapped_keys = set()

    for p in sorted(graph_dir.glob("*.md")):
        name = p.stem
        filenames[name.lower()] = name
        fm = extract_frontmatter(p.read_text(encoding="utf-8"))
        if fm is None:
            if p.read_text(encoding="utf-8").startswith("---"):
                parse_errors.append(name)
            notes[name] = {}
            continue
        if not isinstance(fm, dict):
            notes[name] = {}
            continue
        rels = {}
        for key, value in fm.items():
            canon = RELATION_MAP.get(key)
            if canon is None:
                unmapped_keys.add(key)
                continue
            targets = parse_targets(value)
            if targets:
                rels.setdefault(canon, []).extend(targets)
        notes[name] = rels

    return notes, filenames, parse_errors, unmapped_keys


def build_atom_maps(notes, filenames):
    atom_of = {}
    name_of = {}

    def register(name):
        if name in atom_of:
            return atom_of[name]
        slug = slugify(name)
        if slug in name_of:
            i = 2
            while f"{slug}_{i}" in name_of:
                i += 1
            slug = f"{slug}_{i}"
        atom_of[name] = slug
        name_of[slug] = name
        return slug

    for name in notes:
        register(name)

    for name, rels in notes.items():
        for targets in rels.values():
            for t in targets:
                resolved = filenames.get(t.lower(), t)
                if resolved not in atom_of:
                    register(resolved)

    return atom_of, name_of


def resolve_target(target, filenames):
    return filenames.get(target.lower(), target)


class ReasonerBackend:
    def __init__(self):
        from semantica.reasoning import DatalogReasoner
        self._engine = DatalogReasoner()
        self._fact_count = 0

    def add_fact(self, fact_str):
        self._engine.add_fact(fact_str)
        self._fact_count += 1

    def add_rule(self, rule_str):
        self._engine.add_rule(rule_str)

    def query(self, query_str):
        return self._engine.query(query_str)

    @property
    def fact_count(self):
        return self._fact_count


def load_reasoner(notes, filenames, atom_of):
    engine = ReasonerBackend()
    self_loops = []
    broken_links = []
    note_names = set(notes.keys())

    for name in notes:
        engine.add_fact(f"concept({atom_of[name]})")

    for name, rels in notes.items():
        src = atom_of[name]
        for rel, targets in rels.items():
            for t in targets:
                resolved = resolve_target(t, filenames)
                tgt = atom_of[resolved]
                if src == tgt:
                    self_loops.append((name, rel))
                    continue
                engine.add_fact(f"{rel}({src}, {tgt})")
                if resolved not in note_names:
                    broken_links.append((name, rel, resolved))

    for rule in SKOS_RULES:
        engine.add_rule(rule)

    return engine, self_loops, broken_links


def find_orphans(notes):
    has_edges = set()
    for name, rels in notes.items():
        if rels:
            has_edges.add(name)
        for targets in rels.values():
            for t in targets:
                has_edges.add(t)
    return sorted(set(notes.keys()) - has_edges)


def run_query(engine, query_str, atom_of, name_of, raw=False):
    if not raw:
        m = re.match(r"(\w+)\((.+)\)", query_str)
        if m:
            pred = m.group(1)
            raw_args = [a.strip() for a in m.group(2).split(",")]
            converted_args = []
            for a in raw_args:
                if a.startswith("?"):
                    converted_args.append(a)
                else:
                    slug = atom_of.get(a)
                    if slug is None:
                        for name, s in atom_of.items():
                            if name.lower() == a.lower():
                                slug = s
                                break
                    converted_args.append(slug if slug else slugify(a))
            query_str = f"{pred}({', '.join(converted_args)})"

    results = engine.query(query_str)
    if not raw:
        for row in results:
            for k, v in row.items():
                if v in name_of:
                    row[k] = name_of[v]
    return results


def cmd_infer(args):
    notes, filenames, _, _ = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, _, _ = load_reasoner(notes, filenames, atom_of)

    if not SKOS_RULES:
        print("No rules defined in SKOS_RULES. Edit scripts/reason.py to add your Datalog rules.")
        return

    limit = args.limit
    for pred in ["ancestor", "related_s", "narrower", "broader"]:
        results = engine.query(f"{pred}(?X, ?Y)")
        if results:
            print(f"\n{pred}: {len(results)} derived facts")
            for row in results[:limit]:
                x = name_of.get(row["X"], row["X"])
                y = name_of.get(row["Y"], row["Y"])
                print(f"  {x} → {y}")
            if len(results) > limit:
                print(f"  ... ({len(results) - limit} more)")


def cmd_check(args):
    notes, filenames, parse_errors, unmapped = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, self_loops, broken_links = load_reasoner(notes, filenames, atom_of)
    orphans = find_orphans(notes)
    findings = 0

    if parse_errors:
        findings += len(parse_errors)
        print(f"\n⚠ YAML parse errors ({len(parse_errors)}):")
        for n in parse_errors:
            print(f"  {n}.md")

    if self_loops:
        findings += len(self_loops)
        print(f"\n⚠ Self-loops ({len(self_loops)}):")
        for name, rel in self_loops:
            print(f"  {name}: {rel} → itself")

    if broken_links:
        findings += len(broken_links)
        print(f"\n⚠ Broken wikilink targets ({len(broken_links)}):")
        for name, rel, target in broken_links[:20]:
            print(f"  {name}: {rel} → [[{target}]] (no matching note)")
        if len(broken_links) > 20:
            print(f"  ... ({len(broken_links) - 20} more)")

    if orphans:
        findings += len(orphans)
        print(f"\n⚠ Orphan concepts ({len(orphans)}) — no edges in or out:")
        for n in orphans[:20]:
            print(f"  {n}")
        if len(orphans) > 20:
            print(f"  ... ({len(orphans) - 20} more)")

    if SKOS_RULES:
        for check_name, label in [
            ("in_cycle", "Broader cycles (concept is its own ancestor)"),
            ("conflict", "Related + OppositeOf conflicts"),
            ("s27_violation", "SKOS S27 violations (related + hierarchical)"),
        ]:
            results = engine.query(f"{check_name}(?X, ?Y)") if check_name != "in_cycle" else engine.query(f"{check_name}(?X)")
            if results:
                findings += len(results)
                print(f"\n⚠ {label} ({len(results)}):")
                for row in results[:20]:
                    if "Y" in row:
                        x = name_of.get(row["X"], row["X"])
                        y = name_of.get(row["Y"], row["Y"])
                        print(f"  {x} ↔ {y}")
                    else:
                        x = name_of.get(row["X"], row["X"])
                        print(f"  {x}")
    else:
        print("\nNote: No SKOS_RULES defined — skipping cycle/conflict/S27 checks.")

    if unmapped:
        print(f"\nℹ Unmapped frontmatter keys (ignored): {', '.join(sorted(unmapped))}")

    if findings == 0:
        print("\n✓ No issues found.")
    else:
        print(f"\n{findings} total findings.")
        sys.exit(1)


def cmd_query(args):
    notes, filenames, _, _ = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, _, _ = load_reasoner(notes, filenames, atom_of)

    results = run_query(engine, args.query, atom_of, name_of, raw=args.raw)
    if not results:
        print("No results.")
    else:
        print(f"{len(results)} results:")
        for row in results:
            print("  " + ", ".join(f"{k}={v}" for k, v in row.items()))


def cmd_report(args):
    STATS_DIR.mkdir(exist_ok=True)
    notes, filenames, parse_errors, unmapped = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, self_loops, broken_links = load_reasoner(notes, filenames, atom_of)
    orphans = find_orphans(notes)

    lines = ["# Reasoning Report\n"]

    total_facts = engine.fact_count
    total_concepts = len(notes)
    total_edges = sum(len(t) for rels in notes.values() for t in rels.values())
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Concepts | {total_concepts} |")
    lines.append(f"| Asserted edges | {total_edges} |")
    lines.append(f"| Loaded facts | {total_facts} |")
    lines.append(f"| Rules | {len(SKOS_RULES)} |")

    if SKOS_RULES:
        lines.append(f"\n## Inferred relations\n")
        for pred in ["ancestor", "related_s", "narrower", "broader"]:
            results = engine.query(f"{pred}(?X, ?Y)")
            if results:
                lines.append(f"- **{pred}**: {len(results)} derived facts")

    lines.append(f"\n## Findings\n")

    if parse_errors:
        lines.append(f"### YAML parse errors ({len(parse_errors)})\n")
        for n in sorted(parse_errors):
            lines.append(f"- {n}.md")

    if self_loops:
        lines.append(f"\n### Self-loops ({len(self_loops)})\n")
        for name, rel in sorted(self_loops):
            lines.append(f"- {name}: {rel}")

    if broken_links:
        lines.append(f"\n### Broken wikilink targets ({len(broken_links)})\n")
        for name, rel, target in sorted(broken_links):
            lines.append(f"- {name}: {rel} → [[{target}]]")

    if orphans:
        lines.append(f"\n### Orphan concepts ({len(orphans)})\n")
        for n in sorted(orphans):
            lines.append(f"- {n}")

    if SKOS_RULES:
        for check_name, label in [
            ("in_cycle", "Broader cycles"),
            ("conflict", "Related + OppositeOf conflicts"),
            ("s27_violation", "SKOS S27 violations"),
        ]:
            if check_name == "in_cycle":
                results = engine.query(f"{check_name}(?X)")
            else:
                results = engine.query(f"{check_name}(?X, ?Y)")
            if results:
                lines.append(f"\n### {label} ({len(results)})\n")
                for row in sorted(results, key=lambda r: tuple(r.values())):
                    if "Y" in row:
                        x = name_of.get(row["X"], row["X"])
                        y = name_of.get(row["Y"], row["Y"])
                        lines.append(f"- {x} ↔ {y}")
                    else:
                        x = name_of.get(row["X"], row["X"])
                        lines.append(f"- {x}")

    if unmapped:
        lines.append(f"\n## Unmapped frontmatter keys\n")
        for k in sorted(unmapped):
            lines.append(f"- `{k}`")

    report = "\n".join(lines) + "\n"
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Report written to {REPORT_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Formal reasoning over the knowledge glossary")
    sub = parser.add_subparsers(dest="command")

    p_infer = sub.add_parser("infer", help="Show inferred relations")
    p_infer.add_argument("--limit", type=int, default=10)

    sub.add_parser("check", help="Check SKOS consistency")

    p_query = sub.add_parser("query", help="Run a Datalog query")
    p_query.add_argument("query", help='e.g. "ancestor(AI agent, ?X)"')
    p_query.add_argument("--raw", action="store_true", help="Use raw atom names")

    sub.add_parser("report", help="Generate stats/reasoning_report.md")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return

    {"infer": cmd_infer, "check": cmd_check, "query": cmd_query, "report": cmd_report}[args.command](args)


if __name__ == "__main__":
    main()
