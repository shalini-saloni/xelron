# JSON Sales Summary

## Task

You are given a JSON file at `/data/input.json` containing a list of sales transactions.
Each transaction has the following fields:

- `id` (integer): unique transaction identifier
- `category` (string): product category
- `amount` (float): sale amount in USD
- `units` (integer): number of units sold

Your job is to **aggregate** these records by `category` and write a summary JSON file to `/data/output.json`.

## Output Format

The output must be a JSON object where each key is a category name. The value for each key is an object with:

- `total_amount` (float, rounded to 2 decimal places): sum of all `amount` values for that category
- `total_units` (integer): sum of all `units` values for that category
- `transaction_count` (integer): number of transactions in that category

The categories in the output must be sorted **alphabetically** by key.

## Example

Given input:
```json
[
  {"id": 1, "category": "Books",       "amount": 12.99, "units": 2},
  {"id": 2, "category": "Electronics", "amount": 199.99, "units": 1},
  {"id": 3, "category": "Books",       "amount": 8.49,  "units": 1}
]
```

Expected output:
```json
{
  "Books": {
    "total_amount": 21.48,
    "total_units": 3,
    "transaction_count": 2
  },
  "Electronics": {
    "total_amount": 199.99,
    "total_units": 1,
    "transaction_count": 1
  }
}
```

## Notes

- Read from `/data/input.json`
- Write the result to `/data/output.json`
- Ensure `total_amount` is rounded to exactly 2 decimal places
- Output keys must be sorted alphabetically
