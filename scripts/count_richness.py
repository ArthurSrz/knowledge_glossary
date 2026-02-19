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
    """Generate dual-axis line graph from stats data."""
    if not data:
        print("No data to plot")
        return

    dates = [datetime.strptime(d["date"], "%Y-%m-%d") for d in data]
    stubs = [d["stubs"] for d in data]
    medium = [d["medium"] for d in data]
    rich = [d["rich"] for d in data]
    links = [d["links"] for d in data]
    avg_scores = [d["avg_score"] for d in data]

    # Create figure with dual axes
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Left axis: File counts
    color1 = '#1f77b4'
    ax1.set_xlabel('Date', fontsize=11)
    ax1.set_ylabel('File Count', color=color1, fontsize=11)

    line1 = ax1.plot(dates, rich, color='#2ca02c', marker='o', linewidth=2, label='Rich (200+ words)')
    line2 = ax1.plot(dates, medium, color='#ff7f0e', marker='s', linewidth=2, label='Medium (50-199 words)')
    line3 = ax1.plot(dates, stubs, color='#d62728', marker='^', linewidth=2, label='Stubs (<50 words)')

    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3)

    # Right axis: Metrics (wikilinks + avg score)
    ax2 = ax1.twinx()
    color2 = '#9467bd'
    ax2.set_ylabel('Knowledge Graph Metrics', color=color2, fontsize=11)

    line4 = ax2.plot(dates, links, color='#17becf', marker='D', linewidth=2, linestyle='--', label='Total Wikilinks')
    line5 = ax2.plot(dates, avg_scores, color='#bcbd22', marker='*', linewidth=2, linestyle='--', markersize=12, label='Avg Richness Score')

    ax2.tick_params(axis='y', labelcolor=color2)

    # Format x-axis dates
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate(rotation=45, ha='right')

    # Combined legend
    lines = line1 + line2 + line3 + line4 + line5
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=10)

    # Title
    plt.title('Knowledge Graph Growth & Richness Over Time', fontsize=13, fontweight='bold')
    fig.tight_layout()

    # Save
    plt.savefig(CHART_FILE, dpi=150, bbox_inches='tight')
    print(f"Saved chart to {CHART_FILE}")
    plt.close()


def main():
    """Main workflow: analyze, store, and visualize."""
    print("Analyzing knowledge graph...")
    stats = analyze_files()

    print("\nAppending to stats history...")
    data = append_stats(stats)

    print("\nGenerating chart...")
    plot_stats(data)

    print("\nDone!")


if __name__ == "__main__":
    main()
