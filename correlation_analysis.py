import pandas as pd
import plotly.express as px

cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Select Relevant Categories
cpi_categories = cpi_data[['Cereals and products', 'Meat and fish', 'Egg', 'Milk and products', 'Oils and fats',
'Fruits', 'Vegetables', 'Fuel and light', 'Housing', 'Health', 'Transport and communication',
'Recreation and amusement', 'Education', 'Personal care and effects', 'Miscellaneous', 'General index']]
cpi_categories = cpi_categories.apply(pd.to_numeric, errors='coerce')

# Compute Correlation
correlation_matrix = cpi_categories.corr()

# Plot Heatmap
fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='RdBu_r', zmin=-1, zmax=1,
                title='Correlation between CPI Categories and General Index')
fig.update_layout(xaxis_title='CPI Category', yaxis_title='CPI Category')

# Save Plot
fig.write_html(r"D:\python projects\Customer Price Analysis\results\correlation_analysis.html")
