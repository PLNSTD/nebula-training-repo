import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("sales_data.csv")
print(df)
# Extract data
regions = df["Region"]
sales = df["Sales"]

# Create a pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom colors
explode = (0.01, 0.05, 0.01, 0.01)  # "Exploding" the first slice

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title("Enhanced Sales Distribution by Region")
plt.savefig('customized_sales_pie_chart.png')
plt.show()