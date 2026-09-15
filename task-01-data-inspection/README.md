# Task 01: Inspect One BTC Data File

## Why this task exists

Before we analyse data or look for trading patterns, we need to understand what one dataset contains. This task is only about reading and describing a single file.

## File to inspect

Only use this file:

```text
data/btc-trading-data-json/trade_events.json
```

Do not inspect the other files yet. Do not modify anything in `/data`.

## What is inside the file

The JSON file has a wrapper object. The actual trading-event rows are in:

```python
payload["records"]
```

Each item in `records` is one simulated BTC trade execution. The timestamp field for this task is `createdAt`.

## Your goal

Complete the TODOs in `solution.py`, then run:

```bash
uv run python task-01-data-inspection/solution.py
```

Your program must print all of the following:

1. Number of records.
2. Field names.
3. A simple type description for every field, similar to a TypeScript interface. For example: `vwap: float` or `netQuoteAmount: float | null`.
4. The first 3 records as sample rows.
5. The oldest `createdAt` value.
6. The newest `createdAt` value.

## Starter code

`solution.py` already gives you:

- the correct path to the data file;
- imports you need;
- small functions to complete one at a time;
- pseudocode comments inside each TODO;
- the `main()` function that calls everything in the right order.

Do not rename or remove the starter functions. Add your code only where a `TODO` is shown. You may add comments if something is unclear.

## Rules

- Use only Python's built-in modules for this task. Do not add dependencies.
- Read the data; never edit, move, rename, or delete it.
- Do not create sample or fake data.
- Keep your work inside this task folder.
- Do not do trading analysis yet. This is only data inspection.

## When you are done

1. Run the command above and check that every required item is printed.
2. Commit and push your completed `solution.py`.
3. Wait for the next assigned task.
