"""
CSV Data Summarizer - Core Analysis Script
Automatically detects data type and runs relevant analyses + visualizations.
Usage: python analyze.py <path_to_csv>
"""

import sys
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = "/tmp/csv_charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Helpers ────────────────────────────────────────────────────────────────────

def detect_date_columns(df):
    date_cols = []
    for col in df.columns:
        if any(kw in col.lower() for kw in ['date', 'time', 'timestamp', 'created', 'updated', 'ordered']):
            try:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
                date_cols.append(col)
            except Exception:
                pass
    return date_cols

def detect_data_type(df):
    cols = " ".join(df.columns.str.lower())
    if any(k in cols for k in ['revenue', 'order', 'sales', 'product', 'sku', 'quantity']):
        return "sales"
    if any(k in cols for k in ['customer', 'segment', 'region', 'age', 'gender', 'churn']):
        return "customer"
    if any(k in cols for k in ['amount', 'transaction', 'balance', 'price', 'cost', 'profit']):
        return "financial"
    if any(k in cols for k in ['timestamp', 'status', 'event', 'metric', 'log', 'error']):
        return "operational"
    if any(k in cols for k in ['rating', 'response', 'score', 'likert', 'survey', 'feedback']):
        return "survey"
    return "generic"

def missing_summary(df):
    miss = df.isnull().sum()
    miss_pct = (miss / len(df) * 100).round(2)
    return pd.DataFrame({'Missing Count': miss, 'Missing %': miss_pct}).query('`Missing Count` > 0')

# ── Visualizations ─────────────────────────────────────────────────────────────

def plot_time_series(df, date_col, numeric_cols, data_type):
    df_sorted = df.sort_values(date_col)
    fig, ax = plt.subplots(figsize=(12, 5))
    target = numeric_cols[0] if numeric_cols else None
    if target:
        df_sorted.set_index(date_col)[target].resample('D').sum().plot(ax=ax, color='steelblue')
        ax.set_title(f"{target} Over Time", fontsize=14)
        ax.set_xlabel("Date")
        ax.set_ylabel(target)
    plt.tight_layout()
    path = f"{OUTPUT_DIR}/time_series.png"
    plt.savefig(path, dpi=150)
    plt.close()
    return path

def plot_correlation_heatmap(df, numeric_cols):
    corr = df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax, square=True)
    ax.set_title("Correlation Heatmap", fontsize=14)
    plt.tight_layout()
    path = f"{OUTPUT_DIR}/correlation_heatmap.png"
    plt.savefig(path, dpi=150)
    plt.close()
    return path

def plot_top_categories(df, cat_col, value_col=None):
    if value_col and value_col in df.columns:
        top = df.groupby(cat_col)[value_col].sum().nlargest(10)
        ylabel = value_col
    else:
        top = df[cat_col].value_counts().head(10)
        ylabel = "Count"
    fig, ax = plt.subplots(figsize=(10, 5))
    top.plot(kind='bar', ax=ax, color='teal', edgecolor='white')
    ax.set_title(f"Top 10: {cat_col}", fontsize=14)
    ax.set_xlabel(cat_col)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    path = f"{OUTPUT_DIR}/top_categories.png"
    plt.savefig(path, dpi=150)
    plt.close()
    return path

def plot_numeric_distributions(df, numeric_cols):
    cols_to_plot = numeric_cols[:6]  # max 6
    n = len(cols_to_plot)
    if n == 0:
        return None
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 4))
    if n == 1:
        axes = [axes]
    for ax, col in zip(axes, cols_to_plot):
        df[col].dropna().plot(kind='hist', bins=30, ax=ax, color='steelblue', edgecolor='white')
        ax.set_title(col, fontsize=11)
        ax.set_xlabel(col)
    plt.suptitle("Numeric Distributions", fontsize=14, y=1.02)
    plt.tight_layout()
    path = f"{OUTPUT_DIR}/distributions.png"
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    return path

def plot_missing_heatmap(df):
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=ax, yticklabels=False)
    ax.set_title("Missing Data Map (yellow = missing)", fontsize=13)
    plt.tight_layout()
    path = f"{OUTPUT_DIR}/missing_data.png"
    plt.savefig(path, dpi=150)
    plt.close()
    return path

# ── Main ───────────────────────────────────────────────────────────────────────

def analyze(file_path):
    print(f"\n{'='*60}")
    print(f"  CSV ANALYSIS REPORT")
    print(f"  File: {os.path.basename(file_path)}")
    print(f"{'='*60}\n")

    # Load
    df = pd.read_csv(file_path)
    date_cols = detect_date_columns(df)
    data_type = detect_data_type(df)
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols = [c for c in df.select_dtypes(include='object').columns if df[c].nunique() < 100]

    # ── 1. Overview ────────────────────────────────────────────────────────────
    print("📊 DATASET OVERVIEW")
    print(f"  Rows        : {df.shape[0]:,}")
    print(f"  Columns     : {df.shape[1]}")
    print(f"  Data Type   : {data_type.capitalize()}")
    print(f"  Numeric cols: {len(numeric_cols)}")
    print(f"  Text cols   : {len(cat_cols)}")
    print(f"  Date cols   : {len(date_cols)}")
    print()

    # ── 2. Columns ─────────────────────────────────────────────────────────────
    print("📋 COLUMN DETAILS")
    for col in df.columns:
        dtype = str(df[col].dtype)
        nulls = df[col].isnull().sum()
        print(f"  {col:<30} {dtype:<15} {nulls} nulls")
    print()

    # ── 3. Stats ───────────────────────────────────────────────────────────────
    if numeric_cols:
        print("📈 NUMERIC STATISTICS")
        stats = df[numeric_cols].describe().round(2)
        print(stats.to_string())
        print()

    # ── 4. Missing Data ────────────────────────────────────────────────────────
    miss_df = missing_summary(df)
    if not miss_df.empty:
        print("⚠️  MISSING DATA")
        print(miss_df.to_string())
        print()
    else:
        print("✅ No missing values found.\n")

    # ── 5. Duplicates ──────────────────────────────────────────────────────────
    dupes = df.duplicated().sum()
    print(f"🔁 Duplicate rows: {dupes:,} ({dupes/len(df)*100:.1f}%)\n")

    # ── 6. Visualizations ─────────────────────────────────────────────────────
    charts = []
    print("🖼️  GENERATING CHARTS")

    if date_cols and numeric_cols:
        p = plot_time_series(df, date_cols[0], numeric_cols, data_type)
        charts.append(p); print(f"  ✔ Time-series chart → {p}")

    if len(numeric_cols) >= 3:
        p = plot_correlation_heatmap(df, numeric_cols)
        charts.append(p); print(f"  ✔ Correlation heatmap → {p}")

    if cat_cols:
        best_cat = max(cat_cols, key=lambda c: df[c].nunique())
        best_val = numeric_cols[0] if numeric_cols else None
        p = plot_top_categories(df, best_cat, best_val)
        charts.append(p); print(f"  ✔ Top categories chart → {p}")

    if numeric_cols:
        p = plot_numeric_distributions(df, numeric_cols)
        if p:
            charts.append(p); print(f"  ✔ Distributions chart → {p}")

    miss_pct = df.isnull().mean().max() * 100
    if miss_pct > 1:
        p = plot_missing_heatmap(df)
        charts.append(p); print(f"  ✔ Missing data heatmap → {p}")

    print()

    # ── 7. Summary insights ────────────────────────────────────────────────────
    print("💡 KEY INSIGHTS")
    insights = []

    if numeric_cols:
        col = numeric_cols[0]
        med = df[col].median()
        mean = df[col].mean()
        skew = "right-skewed" if mean > med * 1.1 else "left-skewed" if mean < med * 0.9 else "roughly symmetric"
        insights.append(f"  • {col}: median={med:,.2f}, mean={mean:,.2f} — distribution is {skew}.")

    if date_cols:
        dc = date_cols[0]
        span = (df[dc].max() - df[dc].min()).days
        insights.append(f"  • Data spans {span} days ({df[dc].min().date()} → {df[dc].max().date()}).")

    if cat_cols:
        cc = cat_cols[0]
        top_val = df[cc].value_counts().idxmax()
        top_pct = df[cc].value_counts(normalize=True).max() * 100
        insights.append(f"  • Most common {cc}: '{top_val}' ({top_pct:.1f}% of rows).")

    if not miss_df.empty:
        worst = miss_df['Missing %'].idxmax()
        worst_pct = miss_df.loc[worst, 'Missing %']
        insights.append(f"  • Highest missing: '{worst}' at {worst_pct}% — consider imputation or removal.")

    if len(numeric_cols) >= 2:
        corr = df[numeric_cols].corr().abs()
        corr_pairs = corr.unstack().sort_values(ascending=False).drop_duplicates()
        corr_pairs = corr_pairs[corr_pairs < 1.0]
        if not corr_pairs.empty:
            top_pair = corr_pairs.idxmax()
            top_val_c = corr_pairs.max()
            insights.append(f"  • Strongest correlation: {top_pair[0]} ↔ {top_pair[1]} (r={top_val_c:.2f}).")

    for insight in insights:
        print(insight)

    print(f"\n{'='*60}")
    print(f"  Analysis complete. {len(charts)} chart(s) saved to {OUTPUT_DIR}")
    print(f"{'='*60}\n")
    return charts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <path_to_csv>")
        sys.exit(1)
    analyze(sys.argv[1])
