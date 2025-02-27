import pandas as pd , os
import plotly.express as px

cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Filter for "Rural+Urban"
rural_urban_cpi = cpi_data[cpi_data['Sector'] == 'Rural+Urban'].sort_values('Date')

# Plot Inflation Trend
fig = px.line(rural_urban_cpi, x='Date', y='General index', title='Inflation Trend Analysis (General CPI Index)')
fig.update_layout(xaxis_title='Date', yaxis_title='CPI - General Index')

# Save Plotimport os
import pandas as pd
import plotly.express as px

# Ensure 'results' directory exists
results_dir = r"D:\python projects\Customer Price Analysis\results"
os.makedirs(results_dir, exist_ok=True)  # Creates the folder if it doesn't exist

# Load data
cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Filter for 'Rural+Urban'
rural_urban_cpi = cpi_data[cpi_data['Sector'] == 'Rural+Urban'].sort_values('Date')

# Plot Inflation Trend
fig = px.line(rural_urban_cpi, x='Date', y='General index', title='Inflation Trend Analysis (General CPI Index)')
fig.update_layout(xaxis_title='Date', yaxis_title='CPI - General Index')

# Save plot
fig.write_html(os.path.join(results_dir, "inflation_trend.html"))

fig.write_html(r"D:\python projects\Customer Price Analysis\results\inflation_trend.html")
