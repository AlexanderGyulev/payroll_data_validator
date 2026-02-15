# Payroll Data Validator

## Overview

This project implements a set of automated validation checks between three input files:

- `GTN.xlsx`
- `Payrun.xlsx`
- `mapping.json`

The validations are implemented in Python using pandas and are covered by pytest unit tests.  
Each validation rule has dedicated positive (passing) and negative (failing) datasets.

---

## Validation Rules Implemented

The following validation rules are implemented:

### 1. The File is of type Excel
Validates that the GTN file can be successfully opened and parsed as an Excel file.

---

### 2. The GTN file contains line breaks (empty lines)
Checks whether the GTN file contains fully empty rows.

---

### 3. The GTN file header structure has changed
Validates that required header columns (based on `mapping.json` where `map = true`) exist in the GTN file.

This detects structural changes such as:
- Missing expected vendor columns
- Header row modifications

Potential improvements in the future:
- Detect duplicated header rows
- Validate header row position explicitly
- Detect unexpected additional header layers

---

### 4. Employees present in Payrun but missing in GTN
Compares employee identifiers between both files and detects employees that exist in the Payrun file but not in the GTN file.

---

### 5. Employees present in GTN but missing in Payrun
Compares employee identifiers between both files and detects employees that exist in GTN but are missing from the Payrun file.

---

### 6. Pay Elements in the GTN file do not have a mapping in the Payrun file
Checks whether pay element columns in the GTN file (columns from index 4 onward) are defined in `mapping.json` (either in `mappings` or `not_used`).

This identifies newly introduced pay elements that are not mapped.

---

### 7. Pay Elements in the Payrun file do not have a mapping in the GTN file
Ensures that all Payrun elements marked with `"map": true` in `mapping.json` have a valid vendor mapping defined.

Potential improvements in the future:
- Validate that the mapped vendor column exists in GTN.xlsx
- Validate that mapped vendor columns correspond to pay element columns (from column index 4 onward)

---

### 8. Pay Elements in the GTN file must contain numeric values
Validates that all non-empty values in GTN pay element columns are numeric.

---

## Running the Tests

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```
