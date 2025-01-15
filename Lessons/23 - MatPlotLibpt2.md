### Sample Data: `student_scores.csv`

First, here is the sample data you should save in a file named `student_scores.csv`:

```csv
Student,Math,English,Science,History
Alice,88,92,85,90
Bob,74,81,78,84
Chloe,97,89,95,91
David,64,73,70,75
Emma,82,88,86,89
```

### Lecture: Visualizing CSV Data with Matplotlib

# 📊 Visualizing CSV Data with Matplotlib

## Part 1: Setup and Data Loading 📁

Matplotlib, combined with Pandas, provides a powerful toolset for visualizing data from CSV files.

### Reading CSV Data

CSV (Comma-Separated Values) files are commonly used to store tabular data. Pandas can easily load this data into Python.

```python
import pandas as pd

# Load data from CSV
data = pd.read_csv('student_scores.csv')
print(data.head())
```

### Sample Data: `student_scores.csv`

Ensure you have the following data saved in a file named `student_scores.csv`:

```csv
Student,Math,English,Science,History
Alice,88,92,85,90
Bob,74,81,78,84
Chloe,97,89,95,91
David,64,73,70,75
Emma,82,88,86,89
```

## Part 2: Introduction to Box Plots 📊

Box plots (or box-and-whisker plots) are used to show the distribution of quantitative data and highlight the median, quartiles, and outliers.

### Why Box Plots?

- They provide a good indication of how the values in the data are spread out.
- Unlike bar graphs, they show outliers, the spread, and the skewness of the data.

### Creating a Box Plot

Visualize the distribution of scores in each subject to compare their performance variations.

```python
import matplotlib.pyplot as plt

# Preparing the data for plotting
subjects = ['Math', 'English', 'Science', 'History']
scores = [data[subject].values for subject in subjects]

# Creating the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(scores, labels=subjects)
plt.title('Student Performance in Different Subjects')
plt.ylabel('Scores')
plt.xlabel('Subjects')
plt.grid(True)
plt.show()
```

## Part 3: Customizing Box Plots 🎨

Discuss how to customize box plots to improve readability and add style.

### Adding Color

```python
plt.figure(figsize=(10, 6))
plt.boxplot(scores, labels=subjects, patch_artist=True,
            boxprops=dict(facecolor='cyan', color='blue'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='red'),
            medianprops=dict(color='yellow'))
plt.title('Colored Box Plot of Student Scores')
plt.ylabel('Scores')
plt.xlabel('Subjects')
plt.grid(True)
plt.show()
```

## Conclusion 🏁

Techniques like box plots can help in quickly understanding data distributions and spotting any outliers or anomalies.
