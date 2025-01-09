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