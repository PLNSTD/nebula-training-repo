## 6. 📦 Composition vs Inheritance

Implement two classes:

- `Box` with an attribute `contents` (a list).
- `ColoredBox` that adds a `color` attribute.

First, implement `ColoredBox` using inheritance from `Box`. Then, implement `ColoredBox` using composition by having a `Box` instance as an attribute.

---

## 7. 📋 Abstract Base Class

Use the `abc` module to create an abstract base class `Shape` with an abstract method `area()`. Then, create subclasses `Circle` and `Rectangle` that implement the `area()` method.

---

## 8. 🌀 Dunder Methods

Create a class `Vector` that represents a vector in 2D space with `x` and `y` coordinates. Implement dunder methods for vector addition `__add__`, string representation `__str__`, and equality comparison `__eq__`.

---

## 9. 🚗 Car Class Hierarchy

Create a class hierarchy for vehicles:

- Base class `Vehicle` with attributes `make` and `model`
- Subclass `Car` with attribute `num_doors`
- Subclass `Truck` with attribute `payload_capacity`

Instantiate objects of `Car` and `Truck`, and demonstrate how they inherit from `Vehicle`.

---

## 10. ⚡ Electric Vehicle Extension

Extend the `Car` class to create an `ElectricCar` subclass with an attribute `battery_capacity`. Override the `start_engine` method to indicate that the car is powered on silently.

---

### Extra Challenge 💡

Combine multiple OOP concepts:

Create an `Employee` class with private attributes, inheritance, and polymorphism:

- Base class `Employee` with a private attribute `__salary` and methods to set and get the salary.
- Subclass `Manager` that overrides a method `calculate_bonus()` differently from the base class.
- Use `@property` decorators to manage access to private attributes.

Then, create multiple employee objects, store them in a list, and write a function that calculates the total salary expenditure.
