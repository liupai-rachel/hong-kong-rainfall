# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

from pathlib import Path
import csv
from datetime import date
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
FILE = HERE / "data" / "hko-daily-rainfall-2026.csv"
OUT = HERE / "out" / "hong-kong-rainfall.png"

with FILE.open(encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

# Skip the title and header rows.
data = rows[3:]

dates = []
rainfall = []

for row in data:
    # Skip empty or incomplete rows.
    if len(row) < 5:
        continue

    year, month, day, value, completeness = row

    # Skip rows without a valid date.
    try:
        current_date = date(int(year), int(month), int(day))
    except ValueError:
        continue

    # "Trace" means a very small amount of rainfall.
    if value.strip().lower() == "trace":
        amount = 0.0
    else:
        try:
            amount = float(value)
        except ValueError:
            continue

    dates.append(current_date)
    rainfall.append(amount)

# Print the first parsed data point before plotting.
print("First parsed data:", dates[0], rainfall[0])
print("Rainfall type:", type(rainfall[0]))

# Create the chart.
plt.figure(figsize=(12, 5))
plt.plot(dates, rainfall)

plt.title("Daily Rainfall in Hong Kong, 2026")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")

plt.xticks(rotation=45)
plt.tight_layout()

# Save the image.
OUT.parent.mkdir(exist_ok=True)
plt.savefig(OUT, dpi=200)
plt.close()

print(f"Saved {OUT}")
