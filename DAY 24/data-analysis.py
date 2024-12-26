import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(0)

# Generate random data
'''data = {
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
    'Sales': np.random.rand(100) * 1000,  # Sales figures between 0 and 1000
    'Transactions': np.random.randint(1, 100, size=100)  # Transactions between 1 and 100
}'''

# Create DataFrame
# df = pd.DataFrame(data)
# df.to_csv('data_region.csv')

# Task 1.1 : Display the first 5 rows of the dataframe
df = pd.read_csv('example_data.csv') # Load from file
selected_by_position = df.iloc[0:5]
print(selected_by_position)

# Task 1.2: Caclulate and display basic statistics for Sales and Transactions columns
transactions_details = df['Transactions'].describe()
sales_details = df['Sales'].describe()
print(pd.DataFrame({'Sales': transactions_details, 'Transactions': sales_details}))

# Task 2.1: Calculate the average sales and transactions per region
regions = df.groupby('Region')
regions_sales_avg = regions['Sales'].mean()
print(regions_sales_avg)

# Task 2.2: Find and display the region with the highest average sales
max_avg = regions_sales_avg.idxmax()
print(max_avg)

# Task 3.1: What is the average sales and transactions figure per region?
avg_sales = df.groupby('Region')['Sales'].mean()
avg_transactions = df.groupby('Region')['Transactions'].mean()
print(avg_sales, avg_transactions)

# Task 3.2: Which region has the highest average sales, and what might this imply?
# Solved by Task 2.2
# That East region has better sales?

# Task 3.3: 