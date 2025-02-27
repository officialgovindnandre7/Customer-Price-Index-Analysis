import pandas as pd
import plotly.graph_objects as go

cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Filter COVID-19 Period
covid_period = cpi_data[(cpi_data['Date'] >= '2020-01-01') & (cpi_data['Date'] <= '2021-12-31')]

fig = go.Figure()
fig.add_trace(go.Scatter(x=covid_period['Date'], y=covid_period['General index'], mode='lines', name='General CPI Index', line=dict(width=2, color='black')))
for sector in ['Fuel and light', 'Health', 'Housing', 'Cereals and products']:
    fig.add_trace(go.Scatter(x=covid_period['Date'], y=covid_period[sector], mode='lines', name=sector))
fig.update_layout(title='CPI Trends During COVID-19', xaxis_title='Date', yaxis_title='CPI Value')

# Save Plot
fig.write_html(r"D:\python projects\Customer Price Analysis\results\event_analysis.html")
