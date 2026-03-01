"""Tests for the json-sales-summary task output."""

import json
import os

OUTPUT_PATH = "/data/output.json"

EXPECTED = {
    "Books": {
        "total_amount": 47.48,
        "total_units": 9,
        "transaction_count": 3,
    },
    "Clothing": {
        "total_amount": 74.45,
        "total_units": 3,
        "transaction_count": 2,
    },
    "Electronics": {
        "total_amount": 538.98,
        "total_units": 4,
        "transaction_count": 3,
    },
    "Toys": {
        "total_amount": 54.98,
        "total_units": 6,
        "transaction_count": 2,
    },
}


def load_output():
    if not os.path.exists(OUTPUT_PATH):
        raise FileNotFoundError(f"Output file not found: {OUTPUT_PATH}")
    with open(OUTPUT_PATH) as f:
        return json.load(f)


def test_output_file_exists():
    assert os.path.exists(OUTPUT_PATH), f"Output file missing: {OUTPUT_PATH}"


def test_output_is_valid_json():
    data = load_output()
    assert isinstance(data, dict), "Output must be a JSON object (dict)"


def test_all_categories_present():
    data = load_output()
    for cat in EXPECTED:
        assert cat in data, f"Missing category: {cat}"


def test_no_extra_categories():
    data = load_output()
    for cat in data:
        assert cat in EXPECTED, f"Unexpected category in output: {cat}"


def test_total_amounts():
    data = load_output()
    for cat, vals in EXPECTED.items():
        actual = data[cat]["total_amount"]
        assert abs(actual - vals["total_amount"]) < 0.01, (
            f"{cat}: expected total_amount={vals['total_amount']}, got {actual}"
        )


def test_total_units():
    data = load_output()
    for cat, vals in EXPECTED.items():
        actual = data[cat]["total_units"]
        assert actual == vals["total_units"], (
            f"{cat}: expected total_units={vals['total_units']}, got {actual}"
        )


def test_transaction_counts():
    data = load_output()
    for cat, vals in EXPECTED.items():
        actual = data[cat]["transaction_count"]
        assert actual == vals["transaction_count"], (
            f"{cat}: expected transaction_count={vals['transaction_count']}, got {actual}"
        )


def test_keys_sorted_alphabetically():
    data = load_output()
    keys = list(data.keys())
    assert keys == sorted(keys), f"Keys not sorted alphabetically: {keys}"


def test_amounts_rounded_to_two_decimals():
    data = load_output()
    for cat, vals in data.items():
        amount = vals["total_amount"]
        assert round(amount, 2) == amount, (
            f"{cat}: total_amount {amount} is not rounded to 2 decimal places"
        )
