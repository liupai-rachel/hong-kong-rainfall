# Process

## 1. Choose the phenomenon

I chose Hong Kong rainfall as my phenomenon because rainfall changes over time and can be clearly represented through data.

## 2. Get the data

I used the 2026 daily total rainfall dataset from the Hong Kong Observatory.

The raw CSV file is saved in the `data/` folder. I kept the original CSV file unchanged so that the project can be reproduced without downloading the data again.

## 3. Prepare the data

In `plot.py`, I read the local CSV file and extracted the date and daily rainfall values.

I converted the rainfall values into numbers so they could be used for visualisation.

Before plotting, I also checked the first row, one rainfall value, and its data type to understand how the CSV data was structured.

## 4. Explore the visual form

I first considered using a simple line chart to show rainfall changes over time. However, I wanted the data to create a stronger visual structure.

I therefore chose a circular visualisation. Each radial line represents one day, while the length of the line changes according to the rainfall amount. This allows the whole year to form one visual pattern.

## 5. What I kept and rejected

I kept the date and daily rainfall amount because they are the main information needed to show how rainfall changes throughout the year.

I rejected other information from the dataset that was not necessary for this visualisation.

I also rejected a geographic map because the dataset does not provide different geographic coordinates for each rainfall value. Instead, I used time as the main structure.

## 6. Final output

The visualisation was created using Python and Matplotlib.

The final image is saved as:

`out/hong-kong-rainfall.png`

The project includes the raw data, script, documentation, and final visualisation so that it can be run again locally.