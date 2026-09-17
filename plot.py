# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

from pathlib import Path
import csv

HERE = Path(__file__).parent
FILE = HERE / "data" / "hko-daily-rainfall-2026.csv"

with FILE.open(encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

# Print it before you plot it
print("First data row:", rows[3])
print("Rainfall value:", rows[3][3])
print("Type:", type(rows[3][3]))
