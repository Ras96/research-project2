import os

import pandas as pd
from matplotlib import pyplot as plt


def plot_gaze(dirname, filename):
    filename_dict = {
        "example1_2d": "Media003.png",
        "example1_3d": "Media002.png",
        "文字メディア": "Media001.png",
        "文字メディア (2)": "Media000.png",
    }
    for name, imgfilename in filename_dict.items():
        for d in ["L", "R"]:
            img = plt.imread(os.path.join("data", dirname, imgfilename))
            plt.imshow(img)
            df = pd.read_csv(os.path.join("data", dirname, filename), header=9)
            df = df[(df["L_GAZE_POINT_ERR"] == 0) & (df["R_GAZE_POINT_ERR"] == 0)]
            df = df.loc[:, ["LX", "LY", "RX", "RY", "MEDIA_NAME"]]
            df = df[
                (df["LX"] >= 0)
                & (df["LX"] <= 1440)
                & (df["LY"] >= 0)
                & (df["LY"] <= 900)
                & (df["RX"] >= 0)
                & (df["RX"] <= 1440)
                & (df["RY"] >= 0)
                & (df["RY"] <= 900)
                & (df["MEDIA_NAME"] == name)
            ]
            plt.plot(df[d + "X"], df[d + "Y"], "o")
            os.makedirs(
                os.path.join(
                    "dist",
                    "plot_gaze",
                    dirname,
                ),
                exist_ok=True,
            )
            plt.savefig(os.path.join("dist", "plot_gaze", dirname, d + "_" + imgfilename))
            plt.clf()


for group in sorted(os.listdir("data")):
    for subject_and_time in sorted(os.listdir(os.path.join("data", group))):
        for filename in os.listdir(os.path.join("data", group, subject_and_time)):
            if filename == "Data.csv":
                plot_gaze(os.path.join(group, subject_and_time), filename)
