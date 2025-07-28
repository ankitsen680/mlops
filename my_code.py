import pandas as pd
import os

# Create a dictionary with friend data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
}

# Convert to a DataFrame (like a table)
df = pd.DataFrame(data)

# Create a 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the DataFrame as a CSV file in the 'data' folder
file_path = os.path.join('data', 'data.csv')
df.to_csv(file_path, index=False)
