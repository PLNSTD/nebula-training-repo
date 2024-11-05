from functools import reduce
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 40}
]
max_age = reduce(lambda a, b: a['age'] if a['age'] > b['age'] else b['age'], people)

print(max_age)