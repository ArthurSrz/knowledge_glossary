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
    """Generate simplified dual-axis line graph: total files (left) vs wikilinks (right)."""
    if not data:
        print("No data to plot")
        return

    dates = [datetime.strptime(d["date"], "%Y-%m-%d") for d in data]
    total_files = [d["total"] for d in data]
    links = [d["links"] for d in data]

    def smart_ylim(values):
        """Compute y-axis limits that show progression clearly with round numbers."""
        lo, hi = min(values), max(values)
        data_range = hi - lo
        # Use at least 10% of the mean as visible range so flat data still gets context
        margin = max(data_range, 0.1 * ((lo + hi) / 2)) * 0.5
        raw_lo = lo - margin
        raw_hi = hi + margin
        # Round to nice step size
        span = raw_hi - raw_lo
        step = 10 ** int(f"{span:.0e}".split("e+")[-1])  # order of magnitude
        nice_lo = max(0, int(raw_lo / step) * step)
        nice_hi = int(raw_hi / step + 1) * step
        return nice_lo, nice_hi

    # Create figure with dual axes
    fig, ax1 = plt.subplots(figsize=(11, 5))

    # Left axis: Total files
    color1 = '#2ca02c'
    ax1.set_xlabel('Date', fontsize=11)
    ax1.set_ylabel('Total Concepts (Files)', color=color1, fontsize=11, fontweight='bold')

    line1 = ax1.plot(dates, total_files, color=color1, marker='o', linewidth=2.5, markersize=7, label='Total Concepts')

    ax1.set_ylim(smart_ylim(total_files))
    ax1.ticklabel_format(axis='y', useOffset=False, style='plain')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.2)

    # Right axis: Wikilinks
    ax2 = ax1.twinx()
    color2 = '#1f77b4'
    ax2.set_ylabel('Total Wikilinks', color=color2, fontsize=11, fontweight='bold')

    line2 = ax2.plot(dates, links, color=color2, marker='s', linewidth=2.5, markersize=7, label='Total Wikilinks')

    ax2.set_ylim(smart_ylim(links))
    ax2.ticklabel_format(axis='y', useOffset=False, style='plain')
    ax2.tick_params(axis='y', labelcolor=color2)

    # Format x-axis dates
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate(rotation=45, ha='right')

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=10)

    # Title
    plt.title('Knowledge Graph Growth: Concepts vs Connectivity', fontsize=12, fontweight='bold')
    fig.tight_layout()

    # Save
    plt.savefig(CHART_FILE, dpi=150, bbox_inches='tight')
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

    # Replace the hardcoded count with the current count
    # Pattern: "containing **[number] interconnected concepts**"
    updated = re.sub(
        r'containing \*\*\d+ interconnected concepts\*\*',
        f'containing **{total_count} interconnected concepts**',
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
