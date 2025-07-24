import pandas as pd
df = pd.read_excel("10Kdata.xlsx")
def revenue_growth(df):
    return df.groupby(['Company'])['Total revenue'].pct_change() * 100
def net_income_growth(df):
    return df.groupby(['Company'])['Net Income'].pct_change() * 100
def avg_metrics():
    return df.groupby('Company')[['Total revenue', 'Net Income']].mean()
def yearly_totals():
    return df.groupby('Year')[['Total revenue', 'Net Income']].sum()