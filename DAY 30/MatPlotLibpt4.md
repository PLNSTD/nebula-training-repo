### Lecture: Creating and Customizing Pie Charts with Matplotlib 🥧

---

## **Part 1: Introduction to Pie Charts**

Pie charts are a great way to visualize proportional data as slices of a circular graph. However, they should be used sparingly and only when the data represents parts of a whole.

---

## **Part 2: Setting Up the Data**

We’ll use sample data representing the distribution of sales across different regions.

### Sample Data

| Region | Sales ($) |
| ------ | --------- |
| North  | 15000     |
| South  | 20000     |
| East   | 17000     |
| West   | 18000     |

Save this data in a file called `sales_data.csv`:

```csv
Region,Sales
North,15000
South,20000
East,17000
West,18000
```

---

## **Part 3: Basic Pie Chart**

Let’s create a simple pie chart.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("sales_data.csv")

# Extract data
regions = df["Region"]
sales = df["Sales"]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sales, labels=regions, autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Region")
plt.show()
```

---

## **Part 4: Customizing the Pie Chart**

Enhance the chart's appearance with additional features.

### Customizing the Chart

```python
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom colors
explode = (0.1, 0, 0, 0)  # "Exploding" the first slice

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title("Enhanced Sales Distribution by Region")
plt.show()
```

---

## **Part 5: Saving the Chart**

Save the chart as an image file for use in presentations or reports.

```python
plt.figure(figsize=(8, 8))
plt.pie(sales, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title("Enhanced Sales Distribution by Region")
plt.savefig("sales_distribution_pie_chart.png", dpi=300)
plt.show()
```

---

## Explanation:

sales:
This is the data being represented in the pie chart. Each value in the sales array corresponds to the size of a slice in the chart.

labels=regions:
This assigns labels to the slices. Each label corresponds to the respective value in the sales array. In this case, the regions (e.g., North, South) will appear as labels on the chart.

autopct='%1.1f%%':
This adds percentage labels to the slices, calculated automatically based on the sales data.

%1.1f%%: The percentage is shown with one decimal place (e.g., 25.4%).
%: Indicates it's a percentage.
1.1f: Means 1 digit before the decimal and 1 digit after.
startangle=90:
Rotates the start of the pie chart by 90 degrees. This is useful for aligning the first slice to a specific angle for better readability.

colors=colors:
This specifies the colors for each slice. The colors array contains a list of color codes (e.g., ['#ff9999', '#66b3ff', ...]), applied to the slices in the same order as the sales data.

explode=explode:
This "pulls out" certain slices from the center of the pie. The explode array defines the distance each slice should move from the center:

A value of 0 keeps the slice in place.
A value like 0.1 moves the slice slightly outward (e.g., to highlight the highest sales slice).
shadow=True:
Adds a shadow effect to the pie chart, giving it a more visually appealing and 3D-like appearance.

Example Breakdown:
If sales = [15000, 20000, 17000, 18000] and regions = ['North', 'South', 'East', 'West']:

The slices' sizes correspond to the sales values.
The labels 'North', 'South', 'East', and 'West' are displayed.
Percentages are calculated and shown on each slice (e.g., "25.0%" for a quarter).
The first slice starts at the top (90 degrees).
Each slice is assigned a custom color, and one slice might be "exploded" for emphasis.

---

## **Conclusion**

Pie charts are simple and effective for showing proportional data but can be misleading if the data isn’t well-suited for this visualization type. Always use pie charts thoughtfully and consider alternatives like bar or stacked bar charts for comparisons.

---
