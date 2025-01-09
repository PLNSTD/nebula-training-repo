import pandas as pd
import matplotlib.pyplot as plt

# Task 1
data = pd.read_csv('student_scores.csv')
print(data.head())

# Task 2
subjects = ['Math', 'English', 'Science', 'History']
scores = [data[subject].values for subject in subjects]

general_fig = plt.figure()
plt.boxplot(scores, labels=subjects)
plt.title('Box of scores with subjects')
plt.xlabel('Subjects')
plt.ylabel('Scores')

students = [student for student in data['Student'].values]
for subject in subjects:
    scores = [int(value) for value in data[subject].values]
    print(students)
    print(scores)
    print(len(scores))
    print(len(students))
    fig = plt.figure()
    # Task 3
    plt.boxplot([scores], labels=[subject], patch_artist=True,
                boxprops=dict(facecolor='lightgreen', color='green'), # box and outline color
                whiskerprops=dict(color='gray'), # Line above and below box
                capprops=dict(color='black'), # baseline of the whiskerprops
                medianprops=dict(color='red')
                )
    plt.grid(True)
    plt.title(subject)
    plt.savefig(subject + '_box_plot.png')
    ''' Task 2 Analysis
    Variability: Math - Has the greatest variability
    Highest Median Score: History
'''

plt.show()

# Task 4
'''
With a good data sample it is useful to identify trends based on ages or activities
Health: for viruses
Tech: to know visitors peak hours of a page and publish advertisments based on them by priority
    low visitors: less priority adv
    high visitors: higher priority adv
'''