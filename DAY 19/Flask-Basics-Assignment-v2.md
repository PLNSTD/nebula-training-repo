### **5. Assignment: Flask Backend Fundamentals 📚**

**Objective:** Solidify your understanding of Flask basics by building a backend with dynamic routes, handling POST requests, and custom error responses.

---

#### **Part 1: Create the App**

1. Set up a Flask project.
2. Add a route `/status` that returns a JSON object with a `status` field set to `"OK"`.

---

#### **Part 2: Dynamic Routing**

1. Create a route `/square/<int:number>` that returns the square of the given number in JSON format.

---

#### **Part 3: Handling POST Requests**

1. Add a route `/echo` that accepts JSON data with a `message` field and returns the same message in JSON format.
   - Example input: `{"message": "Hello"}`
   - Example output: `{"echo": "Hello"}`

---

#### **Part 4: Custom Error Handling**

1. Implement a 404 error handler that returns a JSON response: `{"error": "Not found"}`.
2. Implement a 400 error handler for invalid POST data.

---

#### **Bonus Challenges 🌟**

1. Create a route `/add/<int:a>/<int:b>` that returns the sum of two numbers.
2. Modify `/echo` to validate that the input contains a `message` field, returning an error otherwise.

---

**Expected Output:**

- A fully functional backend with:
  - At least 2 dynamic routes.
  - Proper handling of GET and POST requests.
  - Custom error responses for invalid requests.
