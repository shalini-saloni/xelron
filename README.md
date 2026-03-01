# xelron — Harbor Task: JSON Sales Summary

A Harbor benchmark task where an AI agent must read a JSON file of sales transactions,
aggregate them by category, and write a structured summary output.

- **Repo:** [shalini-saloni/xelron](https://github.com/shalini-saloni/xelron)
- **Difficulty:** Easy
- **Topic:** JSON, Data Processing, Aggregation

---

## What the Agent Must Do

1. Read `/data/input.json` — a list of sales transactions
2. Group transactions by `category`
3. For each category, compute:
   - `total_amount` (float, rounded to 2 decimal places)
   - `total_units` (integer)
   - `transaction_count` (integer)
4. Write the result to `/data/output.json`, with keys sorted alphabetically

---

## Folder Structure

```
xelron/
├── README.md                   ← You are here
└── harbor_tasks/
    └── json-sales-summary/
        ├── task.toml           ← Task metadata (name, difficulty, tags)
        ├── instruction.md      ← Instructions shown to the agent
        ├── environment/
        │   ├── Dockerfile      ← Container setup (Python 3.12-slim)
        │   └── input.json      ← 10 sales records across 4 categories
        ├── solution/
        │   ├── solve.py        ← Reference Python solution
        │   └── solve.sh        ← Shell wrapper that runs solve.py
        └── tests/
            ├── test.sh         ← Runs pytest on the output
            └── test_outputs.py ← 9 test cases that validate the output
```

---

## Step-by-Step Setup & Validation Guide

### Step 1 — Prerequisites

Make sure these tools are installed on your machine:

```bash
# Check Docker
docker --version

# Check uv (Python package manager)
uv --version
```

If `uv` is not installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### Step 2 — Clone Your Repo

```bash
git clone https://github.com/shalini-saloni/xelron.git
cd xelron
```

---

### Step 3 — Clone the Harbor Framework (separate)

Harbor's CLI tools live in the official Harbor repo. Clone it alongside your repo:

```bash
git clone https://github.com/laude-institute/harbor.git
cd harbor
```

---

### Step 4 — Copy the Task Into Harbor

Copy the task folder from your `xelron` repo into Harbor's `harbor_tasks/` directory:

```bash
cp -r ../xelron/harbor_tasks/json-sales-summary ./harbor_tasks/
```

Your structure should now look like:

```
harbor/
└── harbor_tasks/
    └── json-sales-summary/     ← copied here
        ├── task.toml
        ├── instruction.md
        ├── environment/
        ├── solution/
        └── tests/
```

---

### Step 5 — Install Harbor Dependencies

Run this once from inside the `harbor/` directory:

```bash
uv sync
```

---

### Step 6 — Run the Oracle Test  (Must Return 1.0)

The Oracle agent runs the reference solution and checks that all tests pass.
This confirms **the task is solvable**.

```bash
uv run harbor run \
  --agent oracle \
  --path harbor_tasks/json-sales-summary \
  --job-name test-oracle
```

 Expected result: **score = 1.0**

---

### Step 7 — Run the NOP Test  (Must Return 0.0)

The NOP agent does nothing. This confirms the task **cannot be auto-passed**.

```bash
uv run harbor run \
  --agent nop \
  --path harbor_tasks/json-sales-summary \
  --job-name test-nop
```

 Expected result: **score = 0.0**

---

### Step 8 — Lint Check (Optional but Recommended)

```bash
uvx ruff check harbor_tasks/json-sales-summary
```

 Expected result: no errors

---

### Step 9 — Push Changes to Your Repo

Once everything passes, commit and push from the `xelron/` directory:

```bash
cd ../xelron
git add .
git commit -m "Add json-sales-summary Harbor task"
git push origin main
```

---

## Input / Output Example

### Input (`environment/input.json`)
```json
[
  {"id": 1, "category": "Electronics", "amount": 299.99, "units": 1},
  {"id": 2, "category": "Books",       "amount": 14.99,  "units": 3},
  {"id": 3, "category": "Clothing",    "amount": 49.95,  "units": 2},
  ...
]
```

### Expected Output (`/data/output.json` — written by agent)
```json
{
  "Books": {
    "total_amount": 47.48,
    "total_units": 9,
    "transaction_count": 3
  },
  "Clothing": {
    "total_amount": 74.45,
    "total_units": 3,
    "transaction_count": 2
  },
  "Electronics": {
    "total_amount": 538.98,
    "total_units": 4,
    "transaction_count": 3
  },
  "Toys": {
    "total_amount": 54.98,
    "total_units": 6,
    "transaction_count": 2
  }
}
```

---

## Test Cases (`tests/test_outputs.py`)

| Test | What it checks |
|---|---|
| `test_output_file_exists` | `/data/output.json` was created |
| `test_output_is_valid_json` | Output is a valid JSON object (dict) |
| `test_all_categories_present` | All 4 categories appear in output |
| `test_no_extra_categories` | No unexpected categories added |
| `test_total_amounts` | Each category's sum is correct (±0.01) |
| `test_total_units` | Each category's unit count is correct |
| `test_transaction_counts` | Each category's record count is correct |
| `test_keys_sorted_alphabetically` | Output keys are A→Z sorted |
| `test_amounts_rounded_to_two_decimals` | Amounts have max 2 decimal places |

---

## Why Oracle Returns 1.0 and NOP Returns 0.0

- **Oracle:** Runs `solution/solve.py` → correctly aggregates all records → all 9 tests pass → score `1.0`
- **NOP:** Does nothing → `/data/output.json` is never created → `test_output_file_exists` fails → score `0.0`

---

## Author

**Shalini Saloni** — [github.com/shalini-saloni](https://github.com/shalini-saloni)  
Repo: [github.com/shalini-saloni/xelron](https://github.com/shalini-saloni/xelron)
