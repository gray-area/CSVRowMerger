# CSV Row Merger

## Overview
This Python script processes a CSV file containing `ID`s and associated text. It merges multiple rows with the same `ID` by combining their text into a single row while ensuring that missing `ID`s are represented as blank rows.

## Features
- **Merges text for duplicate `ID`s**
- **Ensures sequential `ID`s** (fills in missing numbers with blank rows)
- **Handles encoding issues** (ensures proper formatting for CSV files in Excel)
- **Preserves order and structure**

## Requirements
- Python 3.x
- pandas library

### Install Dependencies
```bash
pip install pandas
```

## Usage
1. **Prepare the CSV file**: Ensure your CSV file has columns for `ID` (e.g., column `H`) and `Text` (e.g., column `B`).
2. **Modify column names if needed**: Adjust `id_col` and `text_col` in the script to match your file structure.
3. **Run the script**:
```bash
python MergeRow.py
```
4. **Check the output**: The processed file, `merged.csv`, will be generated in the same directory.

## Example
### Input CSV (`input.csv`)
| H  | B         |
|----|----------|
| 1  | Comment A|
| 2  | Comment B|
| 2  | Comment C|
| 4  | Comment D|
| 8  | Comment E|

### Output CSV (`merged_output.csv`)
| H  | B                 |
|----|------------------|
| 1  | Comment A       |
| 2  | Comment B, Comment C |
| 3  |                  |
| 4  | Comment D       |
| 5  |                  |
| 6  |                  |
| 7  |                  |
| 8  | Comment E       |

## Notes
- The script automatically fills in missing ` ID`s.
- It ensures text is properly formatted and encoded for Excel.

## License
This project is open-source and available under the MIT License.

