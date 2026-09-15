# Task 01: Data Inspection

## Goal

Inspect the historical BTC data provided in `/data` and describe what is available. Do not modify any file in `/data`.

## Your work

Write your solution in `solution.py`. It should:

1. Find every data file in `/data`.
2. Print each file's name and size.
3. For each CSV or Parquet file, print:
   - column names;
   - data types;
   - row count;
   - the first five rows;
   - the earliest and latest timestamp, if a timestamp-like column exists.
4. Clearly report files that cannot be read instead of silently skipping them.

## Rules

- Read data only; do not edit, move, rename, or delete it.
- Do not create sample data.
- Keep the solution in this folder.
- Add comments where your choices are not obvious.

## Deliverable

Commit and push this folder's completed `solution.py` when you finish. Do not start another task unless assigned.
