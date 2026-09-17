# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

from pathlib import Path
import csv
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
FILE = HERE / "data" / "hko-daily-rainfall-2026.csv"
OUT = HERE / "out" / "hong-kong-rainfall.png"

with FILE.open(encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

# The first three rows are the title and header information.
data = rows[3:]

dates = []
rainfall = []

for row in data:
    year, month, day, value, completeness = row

    dates.append(f"{year}-{month}-{day}")
    rainfall.append(float(value))

plt.figure(figsize=(12, 5))
plt.plot(dates, rainfall)

plt.title("Daily Rainfall in Hong Kong, 2026")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")

plt.xticks(rotation=45)
plt.tight_layout()

OUT.parent.mkdir(exist_ok=True)
plt.savefig(OUT, dpi=200)
plt.close()

print(f"Saved {OUT}")
