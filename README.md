# Snooze Button Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/Shanumameyra/snooze-button-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/Shanumameyra/snooze-button-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)

One-line roast of an alarm clock that rings at 6 AM on a Saturday, entered in the
[make.fun Snooze Button Roast bounty](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6).

## The line

> My alarm clock went off at 6 AM on a Saturday like it had a shift to clock into — buddy, even the snooze button called in sick.

(127 characters, one line.)

## How it works

`main.py` writes the line to `/output/entry.txt` (or `$OUTPUT_PATH` when set).
It never writes to the repo unguarded, so it runs fine on the grader's
read-only mount.

```sh
python3 main.py
```
