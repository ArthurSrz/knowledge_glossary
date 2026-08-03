#!/usr/bin/env python3
"""
Analyze knowledge graph richness and generate daily statistics.

Metrics collected:
- Total files
- Stub count (0-49 words)
- Medium count (50-199 words)
- Rich count (200+ words)
- Empty count (0 words)
- Total wikilinks
- Average richness score
"""

import json
import glob
import re
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Configuration
GRAPH_DIR = Path("graph")
STATS_DIR = Path("stats")
DATA_FILE = STATS_DIR / "data.json"
CHART_FILE = STATS_DIR / "chart.png"

STATS_DIR.mkdir(exist_ok=True)


def count_words(text):
    """Count words in text, excluding YAML frontmatter."""
    # Remove YAML frontmatter (content between --- markers)
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    # Split on whitespace and count
    return len(text.split())


def extract_wikilinks(text):
    """Extract all wikilinks [[...]] from text."""
    return len(re.findall(r'\[\[([^\]]+)\]\]', text))


def count_frontmatter_fields(text):
    """Count YAML frontmatter fields."""
    match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return 0
    # Count lines that contain colons (simple heuristic for YAML fields)
    fm = match.group(1)
    return len([line for line in fm.split('\n') if ':' in line and not line.strip().startswith('#')])


def calculate_richness_score(words, fm_fields, links):
    """
    Calculate richness score (0-100).

    Formula: min(100, words/5 + fm_fields*3 + links*2)
    - Every 5 words = 1 point
    - Each frontmatter field = 3 points
    - Each wikilink = 2 points
    """
    if words == 0:
        return 0
    score = (words / 5) + (fm_fields * 3) + (links * 2)
    return min(100, score)


def analyze_files():
    """Analyze all markdown files in graph/ directory."""
    md_files = glob.glob(str(GRAPH_DIR / "*.md"))

    total = len(md_files)
    stubs = 0  # 0-49 words
    medium = 0  # 50-199 words
    rich = 0  # 200+ words
    empty = 0  # 0 words
    total_links = 0
    richness_scores = []

    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        word_count = count_words(content)
        wikilinks = extract_wikilinks(content)
        fm_fields = count_frontmatter_fields(content)
        score = calculate_richness_score(word_count, fm_fields, wikilinks)

        total_links += wikilinks
        richness_scores.append(score)

        if word_count == 0:
            empty += 1
        elif word_count < 50:
            stubs += 1
        elif word_count < 200:
            medium += 1
        else:
            rich += 1

    avg_richness = sum(richness_scores) / len(richness_scores) if richness_scores else 0

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "total": total,
        "empty": empty,
        "stubs": stubs,
        "medium": medium,
        "rich": rich,
        "links": total_links,
        "avg_score": round(avg_richness, 1)
    }


def append_stats(stats):
    """Append stats to data.json (append-only history)."""
    data = []

    # Load existing data if it exists
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)

    # Don't add duplicate entry for today
    if data and data[-1]["date"] == stats["date"]:
        print(f"Stats for {stats['date']} already exist, updating...")
        data[-1] = stats
    else:
        data.append(stats)

    # Write back
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Updated {DATA_FILE}: {stats}")
    return data


def plot_stats(data):
    """Generate modern dark-themed chart with gradient fills."""
    if not data:
        print("No data to plot")
        return

    dates = [datetime.strptime(d["date"], "%Y-%m-%d") for d in data]
    total_files = [d["total"] for d in data]
    links = [d["links"] for d in data]

    def smart_ylim(values):
        lo, hi = min(values), max(values)
        data_range = hi - lo
        margin = max(data_range, 0.1 * ((lo + hi) / 2)) * 0.5
        raw_lo = lo - margin
        raw_hi = hi + margin
        span = raw_hi - raw_lo
        step = 10 ** int(f"{span:.0e}".split("e+")[-1])
        nice_lo = max(0, int(raw_lo / step) * step)
        nice_hi = int(raw_hi / step + 1) * step
        return nice_lo, nice_hi

    BG = '#0d1117'
    SURFACE = '#161b22'
    BORDER = '#30363d'
    TEXT = '#c9d1d9'
    TEXT_DIM = '#8b949e'
    CYAN = '#58a6ff'
    GREEN = '#3fb950'

    fig, ax1 = plt.subplots(figsize=(11, 5))
    fig.patch.set_facecolor(BG)
    ax1.set_facecolor(SURFACE)

    for spine in ax1.spines.values():
        spine.set_color(BORDER)

    ax1.set_ylabel('Concepts', color=GREEN, fontsize=11, fontweight='bold')
    line1 = ax1.plot(dates, total_files, color=GREEN, linewidth=2.5, label='Concepts', zorder=3)
    ax1.fill_between(dates, total_files, alpha=0.08, color=GREEN)
    ax1.set_ylim(smart_ylim(total_files))
    ax1.ticklabel_format(axis='y', useOffset=False, style='plain')
    ax1.tick_params(axis='y', labelcolor=GREEN, colors=TEXT_DIM)
    ax1.tick_params(axis='x', colors=TEXT_DIM)
    ax1.grid(True, alpha=0.1, color=TEXT_DIM, linestyle='--')

    ax2 = ax1.twinx()
    for spine in ax2.spines.values():
        spine.set_color(BORDER)
    ax2.set_ylabel('Wikilinks', color=CYAN, fontsize=11, fontweight='bold')
    line2 = ax2.plot(dates, links, color=CYAN, linewidth=2.5, label='Wikilinks', zorder=3)
    ax2.fill_between(dates, links, alpha=0.06, color=CYAN)
    ax2.set_ylim(smart_ylim(links))
    ax2.ticklabel_format(axis='y', useOffset=False, style='plain')
    ax2.tick_params(axis='y', labelcolor=CYAN, colors=TEXT_DIM)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=10))
    fig.autofmt_xdate(rotation=0, ha='center')

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    legend = ax1.legend(lines, labels, loc='upper left', fontsize=10,
                        facecolor=SURFACE, edgecolor=BORDER, labelcolor=TEXT)

    latest = data[-1]
    summary = f"{latest['total']} concepts  ·  {latest['links']:,} links  ·  {latest['rich']} rich"
    fig.text(0.5, 0.96, summary, ha='center', fontsize=10, color=TEXT_DIM,
             fontstyle='italic')

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig(CHART_FILE, dpi=150, bbox_inches='tight', facecolor=BG)
    print(f"Saved chart to {CHART_FILE}")
    plt.close()


def update_readme(total_count):
    """Update README with current concept count."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("README.md not found, skipping update")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = re.sub(
        r'concepts-\d+-blue',
        f'concepts-{total_count}-blue',
        content
    )

    if updated != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated README.md with concept count: {total_count}")
    else:
        print("README.md already up-to-date")


def main():
    """Main workflow: analyze, store, and visualize."""
    print("Analyzing knowledge graph...")
    stats = analyze_files()

    print("\nAppending to stats history...")
    data = append_stats(stats)

    print("\nGenerating chart...")
    plot_stats(data)

    print("\nUpdating README...")
    update_readme(stats["total"])

    print("\nDone!")


if __name__ == "__main__":
    main()
