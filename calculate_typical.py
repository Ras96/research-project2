import pandas as pd

df = pd.read_csv("dist/analyze_fixation.csv")
df = df.loc[:, ["Time", "Media", "Count", "TotalTime", "TotalDistance"]].groupby(["Time", "Media"], sort=False)
df.mean().round(2).to_csv("dist/calculated_typical_mean.csv")
df.median().round(2).to_csv("dist/calculated_typical_median.csv")
df.std().round(2).to_csv("dist/calculated_typical_std.csv")


