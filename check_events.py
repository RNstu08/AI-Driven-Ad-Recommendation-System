import pandas as pd

# Load the events data
data = pd.read_csv("data/retailrocket/events.csv")

# Display the first few rows and column names to understand the structure
print(data.columns)
print(data.head())
