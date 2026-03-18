# iomyfiles

Python utility library for importing engineering data files — Excel spreadsheets, MATLAB .mat files, and instrument exports with custom headers/formats.

## Features

- Read MATLAB `.mat` files into Python (NumPy arrays / pandas DataFrames)
- Parse Excel files with non-standard headers (instrument exports, lab equipment)
- Handle custom delimiters and multi-header formats common in test equipment output

## Installation

```bash
pip install -e .
```

## Contents

| Path | Description |
|:-----|:------------|
| `iomyfiles/` | Main package |
| `tests/` | Unit tests |

## Requirements

See `requirements.txt`. Core dependencies: NumPy, SciPy, pandas, openpyxl.
