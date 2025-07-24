import pandas as pd
df = pd.read_excel("10Kdata.xlsx")
def revenue_growth():
    df["Revenue Growth"] = df.groupby('Company')['Total revenue'].pct_change() * 100
    return df[["Company", "Year", "Revenue Growth"]]
def net_income_growth():
    df["Net Income Growth"] = df.groupby('Company')['Net Income'].pct_change() * 100
    return df[["Company", "Year", "Net Income Growth"]]
def avg_metrics():
    return df.groupby('Company')[['Total revenue', 'Net Income']].mean()
def yearly_totals():
    return df.groupby('Year')[['Total revenue', 'Net Income']].sum()