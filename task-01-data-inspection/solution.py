"""Task 01: inspect the BTC trade-events dataset."""

import json
from datetime import datetime
from pathlib import Path


# This builds the path from this file, so the script works when run from the
# repository root with the command in the task README.
DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "btc-trading-data-json"
    / "trade_events.json"
)


def load_data() -> dict:
    """Read the JSON file and return its top-level object."""
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def get_records(payload: dict) -> list[dict]:
    """Return the list of trade-event records from the JSON wrapper."""
    return payload["records"]


def get_field_names(records: list[dict]) -> list[str]:
    """Return the field names in one trade-event record."""
    # Look at the first record and return its keys as a list.
    # TODO: write your code here.
    pass


def describe_field_types(records: list[dict]) -> dict[str, str]:
    """Return each field and every type seen for that field."""
    # Inspect the values of every field across the records.
    # Return a readable type for each field, including null where it appears.
    # TODO: write your code here.
    pass


def get_date_range(records: list[dict]) -> tuple[datetime, datetime]:
    """Return the oldest and newest createdAt timestamps."""
    # Convert every createdAt value into a datetime, then find min and max.
    # Hint: datetime.fromisoformat needs "Z" replaced with "+00:00".
    # TODO: write your code here.
    pass


def print_report(records: list[dict], field_types: dict[str, str]) -> None:
    """Print the requested inspection report."""
    # Print the record count, fields with types, first 3 records, and date range.
    # TODO: write your code here.
    pass


def main() -> None:
    """Run the whole task in the correct order."""
    payload = load_data()
    records = get_records(payload)
    field_names = get_field_names(records)
    field_types = describe_field_types(records)
    print("Fields:", field_names)
    print_report(records, field_types)


if __name__ == "__main__":
    main()
