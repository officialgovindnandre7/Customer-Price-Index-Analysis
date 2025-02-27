import pandas as pd
import plotly.graph_objects as go
import os
from statsmodels.tsa.seasonal import seasonal_decompose

# Load data
cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv")

# Ensure 'Date' is in datetime format
cpi_data['Date'] = pd.to_datetime(cpi_data['Date'])
cpi_data.set_index('Date', inplace=True)

# Resample with 'ME' (Month-End)
monthly_cpi = cpi_data['General index'].resample('ME').mean().interpolate(method='linear')

# Ensure enough data points for seasonal decomposition (at least 24 months)
if len(monthly_cpi) >= 24:
    decomposition = seasonal_decompose(monthly_cpi, model='multiplicative', period=12)

    # Create the 'results' directory if it doesn't exist
    results_dir = r"D:\python projects\Customer Price Analysis\results"
    os.makedirs(results_dir, exist_ok=True)

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=decomposition.observed.index, y=decomposition.observed, mode='lines', name='Observed'))
    fig.add_trace(go.Scatter(x=decomposition.trend.index, y=decomposition.trend, mode='lines', name='Trend'))
    fig.add_trace(go.Scatter(x=decomposition.seasonal.index, y=decomposition.seasonal, mode='lines', name='Seasonal'))
    fig.add_trace(go.Scatter(x=decomposition.resid.index, y=decomposition.resid, mode='lines', name='Residual'))
    
    fig.update_layout(title='Seasonal Decomposition of CPI', xaxis_title='Date')

    # Save Plot
    output_path = os.path.join(results_dir, "seasonal_analysis.html")
    fig.write_html(output_path)

    print(f"Plot saved at {output_path}")
else:
    print("Not enough data for seasonal decomposition. At least 24 months required.")
