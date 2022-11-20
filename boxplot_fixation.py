import pandas as pd

df = pd.read_csv("dist/analyze_fixation.csv")
df = df.loc[:, ["Time", "Media", "Count", "TotalTime", "TotalDistance"]]
df.boxplot(by=["Media", "Time"], column=["Count"], grid=False, showmeans=True, whis=1.5).get_figure().savefig(
    "dist/boxplot_fixation_count.png"
)
df.boxplot(by=["Media", "Time"], column=["TotalTime"], grid=False, showmeans=True, whis=1.5).get_figure().savefig(
    "dist/boxplot_fixation_totaltime.png"
)
df.boxplot(by=["Media", "Time"], column=["TotalDistance"], grid=False, showmeans=True, whis=1.5).get_figure().savefig(
    "dist/boxplot_fixation_totaldistance.png"
)
