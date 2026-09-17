# Process

## 1. Choose the phenomenon

I chose Hong Kong rainfall because rainfall is a clear phenomenon that changes over time and can be represented visually.

## 2. Get the data

The data was collected from the Hong Kong Observatory open data.

I used the 2026 daily rainfall CSV file.

The raw CSV file is saved in the `data/` folder.

## 3. Prepare the data

The `plot.py` script reads the local CSV file from the `data/` folder.

It extracts the date and daily rainfall values and converts them into data that can be plotted.

## 4. Make the visualisation

I used Python and Matplotlib to create the rainfall visualisation.

The final image is saved as:

`out/hong-kong-rainfall.png`

## 5. Reproducibility

The raw data is included in the repository, so the visualisation can be generated without downloading the data again.

The scripts can be run locally using `uv run`.