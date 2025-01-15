# Conditions and Control Flow

### Objectives
- Understand the concept and use of conditional statements in Python.
- Learn to implement decision-making using `if`, `else`, and `elif`.
- Apply logical operators in conditional statements.
- Explore nesting of conditional statements for complex decision-making.

### 1. Introduction to Conditional Statements
Conditional statements are foundational in programming, enabling decision-making based on specific conditions. In Python, these are implemented using `if`, `else`, and `elif`.

#### Basic Structure
```python
if condition:
    # Code executed if the condition is True
```

The condition is a statement that evaluates whether it is true or false. True leads to the execution of the indented code block.

### 2. Implementing Basic Decision Making
Example:
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
This code asks for age and checks if the person can vote.

### 3. Enhancing Decision-Making with Logical Operators
Logical operators like `and`, `or`, `not` improve decision-making capabilities.

Example:
```python
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
elif num > 0 and num % 2 != 0:
    print("The number is positive and odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```
Multiple conditions are combined using logical operators to classify a number.

### 4. Nesting Conditional Statements
Nested if statements allow for hierarchical decision-making.

Example:
```python
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
```
This code illustrates a two-level decision process about a number.

### Summary
- Conditional statements are vital for decision-making in Python.
- `if`, `else`, and `elif` are used to create these statements.
- Logical operators refine the decision-making process.
- Nesting allows for more complex decisions.

**Conditional Statements Practice and Homework**

**Practice:**

1. **Basic Decision Making:**
   - Write a program to check if a number is positive, negative, or zero.
   - Input: Any integer.
   - Output: A string stating the type of number.

2. **Logical Operators:**
   - Create a program that determines if a year is a leap year. Use logical operators.
   - Input: A year.
   - Output: True if a leap year, False otherwise.

3. **Nested Conditional Statements:**
   - Develop a program that categorizes a person's life stage: child (< 18), adult (18-64), senior (> 64).
   - Input: Age as an integer.
   - Output: The life stage.

**Homework:**

1. **Temperature Converter:**
   - Write a program that converts temperature from Fahrenheit to Celsius and vice versa. Use an `if-elif-else` block to handle both conversions within the same program.
   - Input: Temperature and the unit to convert to (Celsius or Fahrenheit).
   - Output: Converted temperature.

2. **Grading System:**
   - Implement a grading system based on scores: A (90-100), B (80-89), C (70-79), D (60-69), F (<60).
   - Input: Score as a percentage.
   - Output: The corresponding grade.