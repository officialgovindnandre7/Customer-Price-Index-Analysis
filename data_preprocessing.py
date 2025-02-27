import pandas as pd

# Load Data
cpi_data = pd.read_csv(r"D:\python projects\Customer Price Analysis\data\cpi.csv")

# Clean Data
cpi_data['Month'] = cpi_data['Month'].str.strip()
cpi_data['Month'] = cpi_data['Month'].replace('Marcrh', 'March')
cpi_data['Date'] = pd.to_datetime(cpi_data['Year'].astype(str) + '-' + cpi_data['Month'], format='%Y-%B')

# Save cleaned data
cpi_data.to_csv(r"D:\python projects\Customer Price Analysis\data\cpi_cleaned.csv", index=False)
