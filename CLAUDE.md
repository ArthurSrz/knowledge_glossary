# CLAUDE.md

## Learnings

### Chart scaling: use smart y-axis limits, not starting from 0

When plotting time-series data with matplotlib (e.g. `stats/chart.png`), don't start y-axes from 0 — it squishes trends to the top and hides day-to-day progression. Instead, use smart scaling that zooms into the data range with padded, rounded margins. See `smart_ylim()` in `scripts/count_richness.py`.

Also always disable matplotlib's offset/scientific notation (`ax.ticklabel_format(useOffset=False, style='plain')`) so tick labels show actual values like 1770, not `-1.0` with a `+1.77e3` offset.
