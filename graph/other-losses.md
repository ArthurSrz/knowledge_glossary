---
type: Research Note
title: Formatting Losses
description: Checkboxes, threaded comments, print areas, controls, and merged cells — features lost or degraded in conversion.
tags:
  - formatting
  - checkboxes
  - comments
  - print-areas
  - controls
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[Excel vs. Gsheet problem]]"
---

## [[Feature]] Losses

- **Checkboxes**: Sheets checkboxes → `TRUE`/`FALSE` text in [[Excel]]
- **Threaded comments**: May convert to static notes or disappear entirely
- **Print areas and page breaks**: Often don't transfer
- **Repeat header rows**: Lost in conversion
- **ActiveX / Form Controls**: Silently removed
- **Merged cells**: Transfer but can break layout addressing

See also [Conditional Formatting](/formatting/conditional-formatting.md) for formatting-specific conversion issues.
