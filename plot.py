# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

from pathlib import Path
import csv
import math
from datetime import date

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import colormaps


HERE = Path(__file__).parent
FILE = HERE / "data" / "hko-daily-rainfall-2026.csv"
OUT = HERE / "out" / "hong-kong-rainfall.png"


# ==========================================
# 1. READ HONG KONG RAINFALL DATA
# ==========================================

with FILE.open(encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

print("First row:", rows[3])
print("One value:", rows[3][3])
print("Type:", type(rows[3][3]))

dates = []
rainfall = []

for row in rows[3:]:

    if len(row) < 5:
        continue

    year, month, day, value, completeness = row[:5]

    try:
        current_date = date(
            int(year),
            int(month),
            int(day)
        )
    except ValueError:
        continue

    value = value.strip()

    # HKO uses "Trace" for a very small amount of rain.
    if value.lower() == "trace":
        amount = 0.0
    else:
        try:
            amount = float(value)
        except ValueError:
            continue

    dates.append(current_date)
    rainfall.append(amount)


if not dates:
    raise RuntimeError("No rainfall data found.")


# ==========================================
# 2. CHECK THE DATA
# ==========================================

print(
    f"First parsed data: "
    f"{dates[0]} {rainfall[0]}"
)

print(
    f"Rainfall type: "
    f"{type(rainfall[0])}"
)


# ==========================================
# 3. CREATE CIRCULAR DATA VISUALISATION
# ==========================================

fig = plt.figure(
    figsize=(12, 12),
    facecolor="#f4f3ee"
)

ax = fig.add_subplot(
    111,
    polar=True
)

ax.set_facecolor("#f4f3ee")

# January at the top
ax.set_theta_zero_location("N")

# Clockwise direction
ax.set_theta_direction(-1)

# Remove normal polar frame
ax.spines["polar"].set_visible(False)

ax.set_xticks([])
ax.set_yticks([])


# ==========================================
# 4. RAINFALL SCALE
# ==========================================

max_rain = max(rainfall)

norm = Normalize(
    vmin=0,
    vmax=max_rain
)

# Blue-green water palette
cmap = colormaps["viridis"]


def rain_length(value):

    if value <= 0:
        return 0.025

    # Square-root scaling keeps small rainfall visible
    return 0.08 + math.sqrt(value) * 0.17


# ==========================================
# 5. DRAW EVERY DAY
# ==========================================

for current_date, value in zip(
    dates,
    rainfall
):

    day_of_year = (
        current_date.timetuple().tm_yday
    )

    total_days = 366 if (
        current_date.year % 4 == 0
        and (
            current_date.year % 100 != 0
            or current_date.year % 400 == 0
        )
    ) else 365

    angle = (
        2
        * math.pi
        * (day_of_year - 1)
        / total_days
    )

    length = rain_length(value)

    color = cmap(
        norm(value)
    )

    # Main radial line
    ax.plot(
        [angle, angle],
        [1.0, 1.0 + length],
        color=color,
        linewidth=1.5,
        alpha=0.88,
        solid_capstyle="round"
    )

    # Small dot at the end
    ax.scatter(
        angle,
        1.0 + length,
        s=7 if value < 20 else 16,
        color=color,
        alpha=0.9,
        zorder=5
    )


# ==========================================
# 6. INNER CIRCLES
# ==========================================

theta = [
    i * 2 * math.pi / 360
    for i in range(360)
]

for radius, alpha, width in [
    (1.0, 0.35, 1.0),
    (1.5, 0.16, 0.8),
    (2.0, 0.08, 0.8),
]:

    ax.plot(
        theta,
        [radius] * len(theta),
        color="#666666",
        alpha=alpha,
        linewidth=width
    )


# ==========================================
# 7. MONTH DIVIDERS
# ==========================================

month_names = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC"
]

for month in range(1, 13):

    month_date = date(
        2026,
        month,
        1
    )

    day_of_year = (
        month_date
        .timetuple()
        .tm_yday
    )

    angle = (
        2
        * math.pi
        * (day_of_year - 1)
        / 365
    )

    # Divider
    ax.plot(
        [angle, angle],
        [0.96, 2.28],
        color="#555555",
        linewidth=0.7,
        alpha=0.3
    )

    # Month label
    ax.text(
        angle,
        2.43,
        month_names[month - 1],
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#333333"
    )


# ==========================================
# 8. HIGHLIGHT HEAVY RAINFALL
# ==========================================

heavy_threshold = max_rain * 0.65

for current_date, value in zip(
    dates,
    rainfall
):

    if value < heavy_threshold:
        continue

    day_of_year = (
        current_date
        .timetuple()
        .tm_yday
    )

    angle = (
        2
        * math.pi
        * (day_of_year - 1)
        / 365
    )

    r = (
        1.0
        + rain_length(value)
    )

    # Highlight point
    ax.scatter(
        angle,
        r,
        s=65,
        facecolor="#e76f51",
        edgecolor="white",
        linewidth=1.2,
        zorder=10
    )

    # Label only the biggest rainfall events
    if value >= max_rain * 0.80:

        ax.text(
            angle,
            r + 0.16,
            (
                f"{current_date.strftime('%b %d')}\n"
                f"{value:.0f} mm"
            ),
            ha="center",
            va="center",
            fontsize=8,
            fontweight="bold",
            color="#333333",
            zorder=11
        )


# ==========================================
# 9. CENTRE
# ==========================================

ax.text(
    0,
    0,
    "HONG KONG\nRAINFALL",
    ha="center",
    va="center",
    fontsize=19,
    fontweight="bold",
    color="#222222",
    linespacing=1.3
)

ax.text(
    0,
    -0.36,
    "DAILY TOTAL · 2026",
    ha="center",
    va="center",
    fontsize=8,
    color="#777777"
)


# ==========================================
# 10. TITLE
# ==========================================

last_date = dates[-1]

fig.text(
    0.08,
    0.95,
    "DAILY RAINFALL IN HONG KONG",
    fontsize=22,
    fontweight="bold",
    color="#222222"
)

fig.text(
    0.08,
    0.925,
    (
        f"2026 · JANUARY TO "
        f"{last_date.strftime('%d %B')}"
        f" · {len(dates)} DAYS"
    ),
    fontsize=10,
    color="#666666"
)


# ==========================================
# 11. EXPLANATION
# ==========================================

fig.text(
    0.08,
    0.055,
    "Each radial line represents one day.",
    fontsize=9,
    color="#666666"
)

fig.text(
    0.08,
    0.038,
    "Longer lines indicate heavier rainfall.",
    fontsize=9,
    color="#666666"
)

fig.text(
    0.08,
    0.021,
    "Source: Hong Kong Observatory · Daily Total Rainfall",
    fontsize=8,
    color="#888888"
)


# ==========================================
# 12. SAVE
# ==========================================

OUT.parent.mkdir(
    exist_ok=True
)

plt.savefig(
    OUT,
    dpi=220,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

print(
    f"Saved {OUT}"
)

plt.show()