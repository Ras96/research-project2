import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dist/analyze_fixation.csv")
df = df.loc[:, ["Time", "Media", "Count", "TotalTime", "TotalDistance"]]

df.boxplot(by=["Media", "Time"], column=["Count"], grid=False, showmeans=True, whis=1.5)
plt.title("Fixation Count")
plt.savefig("dist/boxplot_fixation_count.png")

df.boxplot(by=["Media", "Time"], column=["TotalTime"], grid=False, showmeans=True, whis=1.5)
plt.title("Fixation Total Time")
plt.savefig("dist/boxplot_fixation_totaltime.png")

df.boxplot(by=["Media", "Time"], column=["TotalDistance"], grid=False, showmeans=True, whis=1.5)
plt.title("Fixation Total Distance")
plt.savefig("dist/boxplot_fixation_totaldistance.png")
