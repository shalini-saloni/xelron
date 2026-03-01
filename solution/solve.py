#!/usr/bin/env python3
"""Reference solution: aggregate sales records by category."""

import json
from collections import defaultdict

INPUT_PATH = "/data/input.json"
OUTPUT_PATH = "/data/output.json"


def main():
    with open(INPUT_PATH) as f:
        transactions = json.load(f)

    summary = defaultdict(lambda: {"total_amount": 0.0, "total_units": 0, "transaction_count": 0})

    for tx in transactions:
        cat = tx["category"]
        summary[cat]["total_amount"] += tx["amount"]
        summary[cat]["total_units"] += tx["units"]
        summary[cat]["transaction_count"] += 1

    # Round amounts and sort alphabetically
    result = {
        cat: {
            "total_amount": round(vals["total_amount"], 2),
            "total_units": vals["total_units"],
            "transaction_count": vals["transaction_count"],
        }
        for cat, vals in sorted(summary.items())
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Summary written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
