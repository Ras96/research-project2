import csv
import os
import re


def analyze_fixation(filename):
    data = {}
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        key = ""
        for row in reader:
            if len(row) == 0 or row[0] == "No":
                continue
            elif row[0].startswith("[M-"):
                key = row[0]
            elif key != "":
                if key not in data:
                    data[key] = []
                data[key].append(
                    {
                        "X": float(row[1]),
                        "Y": float(row[2]),
                        "Start": float(row[3]),
                        "End": float(row[4]),
                    }
                )
    res = {}
    for key, value in data.items():
        res[key] = {
            "Count": len(value),
            "TotalTime": 0,
            "TotalDistance": 0,
        }
        for i in range(len(value)):
            res[key]["TotalTime"] += value[i]["End"] - value[i]["Start"]
            if i > 0:
                res[key]["TotalDistance"] += (
                    (value[i]["X"] - value[i - 1]["X"]) ** 2 + (value[i]["Y"] - value[i - 1]["Y"]) ** 2
                ) ** 0.5
    return res


with open("dist/analyze_fixation.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Group", "Subject", "Time", "Media", "Count", "TotalTime", "TotalDistance"])
    for group in sorted(os.listdir("data")):
        for subject_and_time in sorted(os.listdir(os.path.join("data", group))):
            for filename in os.listdir(os.path.join("data", group, subject_and_time)):
                if filename == "Fixation.csv":
                    res = analyze_fixation(os.path.join("data", group, subject_and_time, filename))
                    for key, value in res.items():
                        groupnum = re.findall(r"\d+", group)[0]
                        subjectnum, timenum = re.findall(r"\d+", subject_and_time)
                        writer.writerow(
                            [
                                groupnum,
                                subjectnum,
                                timenum,
                                key,
                                value["Count"],
                                "{:.2f}".format(value["TotalTime"]),
                                "{:.2f}".format(value["TotalDistance"]),
                            ]
                        )
