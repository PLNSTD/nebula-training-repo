### Numbers in Python

#### Table of Contents

2. **[Delving into Numbers](#2-delving-into-numbers)**

   - [2.1 Distinguishing Between Integers and Floats](#21-distinguishing-between-integers-and-floats)
   - [2.2 Executing Mathematical Operations with Arithmetic Operators](#22-executing-mathematical-operations-with-arithmetic-operators)
   - [2.3 Harnessing Built-In Functions for Mathematical Operations](#23-harnessing-built-in-functions-for-mathematical-operations)
   - [2.4 Comprehending and Manipulating the Order of Operations](#24-comprehending-and-manipulating-the-order-of-operations)
   - [2.5 Utilizing the Math Module for Advanced Mathematical Operations](#25-utilizing-the-math-module-for-advanced-mathematical-operations)
   - [2.6 Generating Random Numbers Using the Random Module](#26-generating-random-numbers-using-the-random-module)

   - [2.7 Handling Infinite Numbers with Float, Decimal Modules and Math Module](#27-handling-infinite-numbers-with-float-decimal-modules-and-math-module)

#### 2. Numbers

**2.1 Distinguishing Between Integers and Floats**

In Python, integers are whole numbers without decimals, e.g., `my_int = 10`. Floating-point numbers, or floats, include decimals, e.g., `my_float = 10.0`.

**2.2 Executing Mathematical Operations with Arithmetic Operators**

Python performs arithmetic with operators like `+`, `-`, `*`, `/`. Example:

```python
sum = 10 + 5
difference = 10 - 5
product = 10 * 5
quotient = 10 / 5
print(sum, difference, product, quotient)  # prints 15 5 50 2.0
```

**2.3 Harnessing Built-In Functions for Mathematical Operations**

Python includes built-in functions for math, such as `abs()` for absolute value, `round()` for rounding, and `pow()` for power. Example:

```python
abs_val = abs(-10)
rounded_val = round(10.6)
power_val = pow(2, 3)
print(abs_val, rounded_val, power_val)  # prints 10 11 8
```

**2.4 Comprehending and Manipulating the Order of Operations**

Python follows BODMAS/PEMDAS rules for operation order. Example:

```python
print(10 + 5 * 2)  # prints 20
print((10 + 5) * 2)  # prints 30
```

**2.5 Utilizing the Math Module for Advanced Mathematical Operations**

For complex math, use Python's math module. Example:

```python
import math
sqrt_val = math.sqrt(16)
print(sqrt_val)  # prints 4.0
```

**2.6 Generating Random Numbers Using the Random Module**

Use Python's random module to generate random numbers. Example:

```python
import random
rand_val = random.randint(1, 10)
print(rand_val)  # prints a random integer between 1 and 10
```

**2.7 Handling Infinite Numbers with Float, Decimal Modules, and Math Module**

Python represents infinite numbers in various ways:

```python
inf_float = float('inf')  # With float
print(inf_float)  # prints inf

inf_math = math.inf  # With math module
print(inf_math)  # prints inf

import decimal
inf_decimal = decimal.Decimal('Infinity')  # With decimal module
print(inf_decimal)  # prints Infinity
```