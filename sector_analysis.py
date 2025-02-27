import pandas as pd
import pandas as pd
import plotly.graph_objects as go
import os

# Load data
cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Ensure 'Date' is in datetime format
cpi_data['Date'] = pd.to_datetime(cpi_data['Date'])

# Define sectors to analyze
sectors_to_analyze = ['Fuel and light', 'Health', 'Housing', 'Cereals and products']

# Select required columns and handle missing values
sector_data = cpi_data[['Date'] + sectors_to_analyze].fillna(method='ffill')

# Create the 'results' directory if it doesn't exist
results_dir = r"D:\python projects\Customer Price Analysis\results"
os.makedirs(results_dir, exist_ok=True)

# Plot CPI trends for selected sectors
fig = go.Figure()
for sector in sectors_to_analyze:
    fig.add_trace(go.Scatter(x=sector_data['Date'], y=sector_data[sector], mode='lines', name=sector))

fig.update_layout(
    title='CPI Trends for Selected Sectors',
    xaxis_title='Date',
    yaxis_title='CPI Value',
    template="plotly_dark"  # Optional: Dark theme for better visibility
)

# Save Plot
output_path = os.path.join(results_dir, "sector_analysis.html")
fig.write_html(output_path)

print(f"Plot saved at {output_path}")

