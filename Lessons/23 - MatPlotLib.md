# 📊 Introduction to Data Visualization with Matplotlib

## Part 1: Installation 🛠️

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

### Steps to Install Matplotlib:

Ensure you have Python and pip already installed. Then run:

```bash
pip install matplotlib
```

## Part 2: Matplotlib Basics 🎨

### Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

### Simple Plot Example

Understand the basic components of a plot—figure, axis, line, labels. Here's a simple example:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Simple Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.show()
```

### Plotting from a DataFrame

Matplotlib integrates well with Pandas, making it a handy tool for plotting data directly from DataFrames. Let's create a `data.csv` file to use in our examples.

### Sample Data for `data.csv`

```csv
id,name,email,age,salary,join_date,department
1,John Doe,john.doe@example.com,28,50000,2020-01-15,Sales
2,Jane Smith,jane.smith@example.com,34,60000,2019-03-22,Marketing
3,Emily Jones,emily.jones@example.com,45,75000,2018-07-13,HR
4,Michael Brown,michael.brown@example.com,23,48000,2021-05-30,Sales
5,Jessica Davis,jessica.davis@example.com,39,69000,2017-09-18,Marketing
6,Daniel Wilson,daniel.wilson@example.com,41,72000,2016-11-25,HR
7,Ashley Martin,ashley.martin@example.com,29,51000,2021-06-19,Sales
8,Chris Lee,chris.lee@example.com,25,45000,2019-12-11,Marketing
```

Save this data into a file named `data.csv`.

## Part 3: Visualizing Data 📊

### Visualizing Salary Distribution by Department

Let's visualize the salary distribution across different departments using a bar chart.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data.csv")

# Aggregate the data by department
salary_by_department = df.groupby("department")["salary"].mean()

# Plot the data
plt.figure(figsize=(10, 5))
salary_by_department.plot(kind='bar', color='skyblue')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.show()
```

### Visualizing Age Distribution

Create a histogram to visualize the age distribution of the employees.

```python
plt.figure(figsize=(10, 5))
plt.hist(df["age"], bins=5, color='green', edgecolor='black')
plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.show()
```

### Scatter Plot: Salary vs. Age

A scatter plot to visualize the relationship between age and salary.

```python
plt.figure(figsize=(10, 5))
plt.scatter(df["age"], df["salary"], color='red')
plt.title("Salary vs. Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
```

### Time Series Analysis: Employee Join Date

Convert the `join_date` to a datetime format and create a time series plot.

```python
df["join_date"] = pd.to_datetime(df["join_date"])

# Plot the number of employees joining over time
plt.figure(figsize=(10, 5))
df.set_index("join_date").resample("M").size().plot(marker='o', linestyle='-')
plt.title("Employee Joining Over Time")
plt.xlabel("Join Date")
plt.ylabel("Number of Employees")
plt.grid(True)
plt.show()
```
