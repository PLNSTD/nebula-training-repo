import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(0)

# Generate a date range
dates = pd.date_range(start="2020-01-01", end="2020-12-31", freq="D")

# Generate synthetic time-series data
data = {
    "Date": dates,
    "Sales": np.random.rand(len(dates)) * 200
    + np.sin(np.linspace(-3, 3, len(dates))) * 50
    + 100,
}

# df = pd.read_csv('example_data.csv')
df = pd.DataFrame(data)
print(df)

# Task 1.1: Display the first 5 rows of the dataset to get an idea of its structure
print(df.iloc[0:5])

# Task 1.2: Generate a quick statistical summary of the Sales column
print(df.describe())

# Task 2.1: Calculate the monthly average sales
df["Date"] = pd.to_datetime(df["Date"])

df.set_index("Date", inplace=True)
monthly_avg = df.resample("M").mean()

print(monthly_avg)

# Task 2.2: Identify any obvious trends in monthly average sales.
'''
First code run, since it is randomized
From Jan-March go down of 20 per month apprx
From Apr-Oct Sales go up to 257
From Nov-Dec Sales go down again
'''

# Task 2.3: Calculate the rolling 7-day avg of sales
df['rolling-7-day-avg'] = df['Sales'].rolling(window=7).mean()
print(df)

# Task 3.1:
# Solved by Task 2.2

# Task 3.2:
# Colder months (autumn and winter) sales drop
# Warmer months (spring and Summer) sales go up

# Task 3.3:
# Idk