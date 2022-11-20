# research-project2

## 事前準備

1. `$PR_USER` `$PR_PASS` `PR_BASEURL`を設定
2. `./download.sh`

## 内容

- `analyze_fixation.py`
  - 各ファイルの`Fixation.csv`を解析して以下のデータを算出し、`dist/analyze_fixation.csv`に出力します
    - 停留点の数
    - 総停留時間
    - 停留点間の総距離
- `calculate_typical.py`
  - **事前に`analyze_fixation.py`の実行が必要です**
  - `analyze_fixation.py`の実行結果から代表値を算出し、以下のファイルに出力します
    - 平均値: `dist/calculate_typical_mean.csv`
    - 中央値: `dist/calculate_typical_median.csv`
    - 標準偏差: `dist/calculate_typical_std.csv`
- `plot_gaze.py`
  - 各ファイルの`Data.csv`から注視点の情報を画像にプロットし、`dist/plot_gaze/`以下に出力します
