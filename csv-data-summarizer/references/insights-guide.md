# Insights Guide — How to Frame CSV Analysis Conclusions

Use this reference when writing the "Key Insights" section of any CSV analysis output.

## Principles

- **Be specific, not vague.** Say "Revenue peaks in Q4, averaging 38% above the annual mean" — not "Sales are seasonal."
- **Quantify everything.** Every insight should have a number attached.
- **Suggest an action.** Each insight should end with what the reader might do next.
- **Rank by impact.** Lead with the most consequential finding, not the most obvious.

## Insight Templates by Data Type

### Sales Data
- "Top product [X] accounts for [N]% of total revenue — concentration risk or a prioritization signal."
- "Month-over-month growth is [+N%] — trending [up/down] since [date]."
- "Average order value is [$X], with the top 10% of orders driving [N]% of total revenue."

### Customer Data
- "[Segment X] represents [N]% of customers but [M]% of revenue — high-value segment worth targeting."
- "Churn rate of [N]% in [region/segment] is [2x/3x] the average — investigate root cause."

### Financial Data
- "Mean transaction value [$X] with std dev [$Y] — [high/low] volatility."
- "Correlation of [r=N] between [A] and [B] suggests [relationship]."

### Generic
- "Column [X] has [N]% missing — imputation or exclusion recommended before modeling."
- "Distribution of [X] is right-skewed (mean >> median) — outliers may be pulling averages up."

## Tone Rules
- Use plain language. Avoid jargon like "heteroscedasticity" unless the user is clearly technical.
- Keep each insight to 1–2 sentences max.
- Don't hedge excessively. "This suggests" is fine; "this might possibly indicate" is not.
