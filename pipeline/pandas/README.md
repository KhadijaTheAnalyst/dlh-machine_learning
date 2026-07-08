# Pandas

This project covers the fundamentals of `pandas`, the core Python library for data manipulation and analysis. Tasks progress from creating `DataFrame` objects from scratch to cleaning, indexing, merging, and visualizing real cryptocurrency trading data (Coinbase and Bitstamp minute-by-minute BTC/USD data).

## Learning Objectives

At the end of this project, you should be able to explain, without Googling:

* What is `pandas`, and what is it used for
* What is a `Series` and what is a `DataFrame`
* How to create a `pd.DataFrame` from various inputs (dict, `np.ndarray`, file)
* How to perform arithmetic and analysis on a `pd.DataFrame`
* How to index a `pd.DataFrame`
* How to use hierarchical indexing (`MultiIndex`) with a `pd.DataFrame`
* How to slice, sort, prune, and fill a `pd.DataFrame`
* How to concatenate, merge, and join `pd.DataFrame` objects
* How to get statistical information from a `pd.DataFrame`
* How to visualize a `pd.DataFrame`

## Requirements

* Python 3.11 (Windows environment, run via `python3.11.exe`)
* All files interpreted/compiled using `python3`
* All files end with a new line
* First line of all files: `#!/usr/bin/env python3`
* Code follows `pycodestyle` style (version 2.x)
* All modules, classes, and functions have documentation (module docstring, function docstring)
* `pandas` version used: `2.x`

## Data Files

Two CSV datasets are used throughout this project (not included in the repo due to size):

| File | Description |
|---|---|
| `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv` | Minute-by-minute Coinbase BTC/USD trading data |
| `bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv` | Minute-by-minute Bitstamp BTC/USD trading data |

Both files share the same column structure: `Timestamp`, `Open`, `High`, `Low`, `Close`, `Volume_(BTC)`, `Volume_(Currency)`, `Weighted_Price`.

## Tasks

| # | File | Description |
|---|---|---|
| 0 | `0-from_numpy.py` | `from_numpy(array)` — creates a `pd.DataFrame` from a `np.ndarray` |
| 1 | `1-from_dictionary.py` | Creates a `pd.DataFrame` (`df`) from a dictionary, with custom column and row labels |
| 2 | `2-from_file.py` | `from_file(filename, delimiter)` — loads data from a file into a `pd.DataFrame` |
| 3 | `3-rename.py` | `rename(df)` — renames `Timestamp` to `Datetime`, converts values to datetime, keeps only `Datetime` and `Close` |
| 4 | `4-array.py` | `array(df)` — selects the last 10 rows of `High` and `Close`, returns as a `numpy.ndarray` |
| 5 | `5-slice.py` | `slice(df)` — extracts `High`, `Low`, `Close`, `Volume_(BTC)`, selects every 60th row |
| 6 | `6-flip_switch.py` | `flip_switch(df)` — sorts data in reverse chronological order and transposes it |
| 7 | `7-high.py` | `high(df)` — sorts the `DataFrame` by `High` price, descending |
| 8 | `8-prune.py` | `prune(df)` — removes rows where `Close` is `NaN` |
| 9 | `9-fill.py` | `fill(df)` — drops `Weighted_Price`, forward-fills `Close`, fills `High`/`Low`/`Open` from `Close`, fills volume columns with `0` |
| 10 | `10-index.py` | `index(df)` — sets the `Timestamp` column as the `DataFrame` index |
| 11 | `11-concat.py` | `concat(df1, df2)` — indexes both DataFrames on `Timestamp`, concatenates Bitstamp data (up to timestamp `1417411920`) on top of Coinbase data, with `keys` labeling each source |
| 12 | `12-hierarchy.py` | `hierarchy(df1, df2)` — rearranges the `MultiIndex` so `Timestamp` is the top level, filters both DataFrames to timestamps `1417411980`–`1417417980`, and returns rows in chronological order |
| 13 | `13-analyze.py` | `analyze(df)` — computes descriptive statistics (`.describe()`) for all columns except `Timestamp` |
| 14 | `14-visualize.py` | Cleans, indexes, fills, and resamples the Coinbase data to daily intervals from 2017 onward, then plots `High`, `Low`, `Open`, `Close`, and both `Volume` columns |

## Key Concepts & Gotchas

A few things worth remembering from working through this project:

* **`df['col']` vs `df[['col']]`** — single brackets return a `Series` (1D); double brackets (a list of column names) always return a `DataFrame` (2D), even for one column.
* **`NaN != NaN`** — you can never detect missing values with `== NaN`. Use `.isna()`, `.isnull()`, or `.dropna()` / `.fillna()` instead.
* **`pd.to_datetime(..., unit='s')`** — when converting Unix epoch integers, always specify the unit; without it, pandas defaults to nanoseconds and silently produces the wrong dates.
* **`&` vs `and`** — combining two boolean row-masks requires the bitwise `&` (with each condition in parentheses), not Python's `and`, because the conditions are element-wise arrays, not single booleans.
* **`pd.concat(..., keys=[...])`** — the order of DataFrames in the list must match the order of labels in `keys`; this produces a `MultiIndex` that can later be reordered with `.reorder_levels()` and sorted with `.sort_index()`.
* **`.resample('D')`** — only works on a `DatetimeIndex`, which is why the data must be indexed on `Date`/`Timestamp` before resampling; paired with `.agg({...})` to apply a different aggregation per column.

## Author

Khadija — Data Analyst, AI Academy @ Digital Learning Hub Luxembourg (Holberton curriculum)