import pandas as pd
import plotly.express as px

cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Compare Sectors
sector_cpi_means = cpi_data.groupby('Sector')['General index'].mean().reset_index()

# Plot
fig = px.bar(sector_cpi_means, x='Sector', y='General index', title='Average CPI Comparison Across Sectors')
fig.update_layout(xaxis_title='Sector', yaxis_title='Average CPI - General Index')

# Save Plot
fig.write_html(r"D:\python projects\Customer Price Analysis\results\sector_comparison.html")
