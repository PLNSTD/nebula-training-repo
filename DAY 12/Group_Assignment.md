# 🚀 Advanced Functional Programming Exercises

## 1. 🧮 Calculate Total Age in Group

Given the following list of people, use `reduce` to calculate the total age of the group.

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 40}
]
```

---

## 2. 🔍 Find the Oldest Person

Using the same `people` list from above, use `reduce` to find the person with the highest age.

---

## 3. 🔠 Extract Unique Job Titles

Given the following list of employees, use `map` and `filter` to extract a list of unique job titles.

```python
employees = [
    {"name": "Alice", "job_title": "Engineer"},
    {"name": "Bob", "job_title": "Designer"},
    {"name": "Charlie", "job_title": "Engineer"},
    {"name": "Diana", "job_title": "Manager"},
    {"name": "Eve", "job_title": "Designer"}
]
```

---

## 4. 🗂️ Filter and Group by Age Range

Using the `people` list, filter out those under 18, then group the remaining people by age range: 18-25, 26-35, 36-45.

---

## 5. 🧩 Merge and Count Job Titles

With the `employees` list, use `reduce` to create an object that counts how many people have each job title.

---

## 6. 📊 Calculate Average Salary

Using the following list of employees with salaries, use `reduce` to calculate the average salary. Exclude any employees with a salary below 50,000.

```python
salaries = [
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 70000},
    {"name": "Diana", "salary": 52000},
    {"name": "Eve", "salary": 48000}
]
```

---

## 7. 🌱 Filter Active Accounts

Given the following list of user accounts, use `filter` to return only active accounts.

```python
accounts = [
    {"name": "Alice", "isActive": True},
    {"name": "Bob", "isActive": False},
    {"name": "Charlie", "isActive": True},
    {"name": "Diana", "isActive": False}
]
```

---

## 8. 🕹️ Generate Usernames

Write a function using `map` to generate usernames from the following list of names in the format `first letter of first name + last name`, all lowercase.

```python
names = [
    {"first_name": "Alice", "last_name": "Johnson"},
    {"first_name": "Bob", "last_name": "Smith"},
    {"first_name": "Charlie", "last_name": "Brown"},
    {"first_name": "Diana", "last_name": "Williams"}
]
```

---

## 9. 📅 Find Longest Employment Duration

Given the following list of employees with `hire_date` and `termination_date`, use `reduce` to find the employee with the longest duration of employment.

```python
employment = [
    {"name": "Alice", "hire_date": "2015-06-01", "termination_date": "2020-06-01"},
    {"name": "Bob", "hire_date": "2012-01-01", "termination_date": "2018-01-01"},
    {"name": "Charlie", "hire_date": "2017-09-01", "termination_date": "2022-09-01"},
    {"name": "Diana", "hire_date": "2013-05-01", "termination_date": "2019-05-01"}
]
```

---

## 10. 📍 Sort Locations by Distance

Using the following list of locations with latitude and longitude, write a function that uses `map` to calculate distances from a reference point `(0, 0)`, then `sort` the list by distance in ascending order.

```python
locations = [
    {"name": "Place A", "latitude": 34.05, "longitude": -118.25},
    {"name": "Place B", "latitude": 40.71, "longitude": -74.01},
    {"name": "Place C", "latitude": 51.51, "longitude": -0.13},
    {"name": "Place D", "latitude": 48.85, "longitude": 2.35}
]
```

---

### Extra Challenge 💡

Combine multiple functional methods (e.g., `map`, `filter`, `reduce`) to process the following data structure, filtering active users, calculating the total age, and grouping by job title.

```python
extended_data = [
    {"name": "Alice", "age": 30, "job_title": "Engineer", "isActive": True},
    {"name": "Bob", "age": 25, "job_title": "Designer", "isActive": False},
    {"name": "Charlie", "age": 35, "job_title": "Engineer", "isActive": True},
    {"name": "Diana", "age": 40, "job_title": "Manager", "isActive": True},
    {"name": "Eve", "age": 28, "job_title": "Designer", "isActive": True}
]
```

---
