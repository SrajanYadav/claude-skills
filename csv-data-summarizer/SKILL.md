---
name: csv-data-summarizer
description: >
  Analyzes CSV files and produces comprehensive summaries — statistics, missing data,
  visualizations, and insights — fully automatically, without asking the user what they want.
  Use this skill IMMEDIATELY whenever a user uploads or mentions a CSV file, asks to summarize
  or analyze tabular data, or says things like "analyze this file", "what's in this CSV",
  "give me insights on this data", or "summarize this spreadsheet". Trigger even if the user
  only says "here's my file" and attaches a CSV. Never wait for further direction — run the
  full analysis right away.
metadata:
  version: 1.0.0
  dependencies: python>=3.8, pandas>=2.0.0, matplotlib>=3.7.0, seaborn>=0.12.0
---

# CSV Data Summarizer

Automatically analyzes CSV files and delivers complete insights — no follow-up questions, no option menus. Just results.

---

## ⚠️ Core Behavioral Rule

**NEVER ask the user what they want to do. NEVER list options. Just run the full analysis immediately.**

❌ Never say:
- "What would you like to do with this data?"
- "Here are some analyses I can run..."
- "Would you like me to create visualizations?"

✅ Always say:
- "I'll analyze this now." → then immediately run the script

---

## Step-by-Step Execution

### Step 1 — Locate the File
- Check `/mnt/user-data/uploads/` for the CSV file
- If not found, ask the user for the file path (this is the ONLY acceptable question)

### Step 2 — Run the Analysis Script
Execute `scripts/analyze.py` with the file path:

```bash
pip install pandas matplotlib seaborn --quiet --break-system-packages
python /home/claude/csv-data-summarizer/scripts/analyze.py "/path/to/file.csv"
```

The script handles everything automatically and saves charts to `/tmp/csv_charts/`.

### Step 3 — Present Results
Structure the output as:

1. **Dataset Overview** — rows, columns, data types
2. **Data Quality** — missing values, duplicates
3. **Key Statistics** — numeric summaries relevant to data type
4. **Visualizations** — charts saved and displayed
5. **Insights** — 3–5 actionable observations from the data

---

## Data Type Detection & Adaptation

The script auto-detects the dataset type and runs only relevant analyses:

| Data Type | Detected By | Key Analyses |
|---|---|---|
| Sales / E-commerce | columns: order, revenue, product, sales | Time trends, top products, revenue stats |
| Customer / CRM | columns: customer, segment, region, age | Demographics, segmentation, geography |
| Financial | columns: amount, transaction, balance, price | Trend, distribution, correlation |
| Operational / Logs | columns: timestamp, status, metric, event | Time-series, status breakdown, performance |
| Survey | columns: rating, response, score, likert | Frequency, distributions, cross-tabs |
| Generic | everything else | Numeric stats, categoricals, correlations |

---

## Visualizations (Only When Applicable)

- **Time-series line chart** → only if date/timestamp column exists
- **Correlation heatmap** → only if 3+ numeric columns exist
- **Top-N bar chart** → only if high-cardinality categorical column exists
- **Numeric histograms** → for all numeric columns (distributions)
- **Missing data heatmap** → if missing values exceed 1%

---

## Reference Files

- `scripts/analyze.py` — Full analysis script (read when running analysis)
- `references/insights-guide.md` — How to phrase insights clearly (read if unsure how to frame conclusions)
