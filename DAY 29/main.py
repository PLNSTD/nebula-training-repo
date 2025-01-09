import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('student_scores.csv')
print(data.head())

# Preparing the data for plotting
subjects = ['Math', 'English', 'Science', 'History']
scores = [data[subject].values for subject in subjects]

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