#!/usr/bin/env bash
# Test runner for json-sales-summary task
set -euo pipefail

echo "=== Running json-sales-summary tests ==="

python3 -m pytest /tests/test_outputs.py -v --tb=short

echo "=== All tests passed ==="
