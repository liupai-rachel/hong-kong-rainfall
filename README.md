# Hong Kong Rainfall

## The phenomenon

This project visualises daily rainfall in Hong Kong during 2026. I chose rainfall as the phenomenon because it changes over time and can create clear differences between dry and rainy periods. The visualisation explores how rainfall is distributed across the year and highlights days with higher rainfall.

## The source

The data comes from the Hong Kong Observatory open data. I used the 2026 daily total rainfall CSV dataset. The dataset records the total rainfall measured each day at the Hong Kong Observatory station.

Source: https://data.weather.gov.hk/weatherAPI/cis/csvfile/HKO/2026/daily_HKO_RF_2026.csv

## What the picture shows

The final visualisation represents the days of 2026 as a circular structure. Each radial line represents one day, and the length of the line changes according to the amount of rainfall. This creates a visual pattern that makes rainy periods and changes across the year easier to notice. Different parts of the circle also correspond to different periods of the year.

## How to run it

The raw CSV file is included in the `data/` folder, so the project does not need to download the data again. Run the plotting script with:

`uv run plot.py`

The final image is saved in:

`out/hong-kong-rainfall.png`