import pandas as pd
import json
import matplotlib.pyplot as plt

with open('student_data.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)
print(df.head())

study_hours = df['Study']
fig1 = plt.figure()
plt.hist(study_hours, bins=5, edgecolor='black')
plt.title('Distribution of Study Hours')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.grid(True)

fig2 = plt.figure()
plt.hist(study_hours, bins=[10, 20, 30, 40, 50], edgecolor='black')
plt.title('Distribution of Study Hours')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.grid(True)

study_hours = df['Sports']
fig1 = plt.figure()
plt.hist(study_hours, bins=6, edgecolor='black')
plt.title('Distribution of Sports Hours bins=6')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.grid(True)

study_hours = df['Sports']
fig1 = plt.figure()
plt.hist(study_hours, bins=5, edgecolor='black')
plt.title('Distribution of Sports Hours bins=5')
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')
plt.grid(True)

plt.show()
