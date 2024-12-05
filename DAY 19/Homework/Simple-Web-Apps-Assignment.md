### **6. Assignment: Building RESTful APIs with Flask 🎯**

**Objective:** Practice building RESTful endpoints, handling POST requests, and structuring consistent API responses.

---

#### **Part 1: Create the App**

1. Add a route `/status` that returns a JSON response with a `status` of `"API is running"`.

---

#### **Part 2: Handle Dynamic Routes**

1. Add a route `/reverse/<string:text>` that returns the reversed version of the `text` string in JSON format.
   - Example: `/reverse/hello` → `{"reversed": "olleh"}`

---

#### **Part 3: POST Requests**

1. Create a route `/sum` that accepts two numbers as JSON fields (`a` and `b`) and returns their sum.

   - Input: `{"a": 5, "b": 7}`
   - Output: `{"sum": 12}`

2. Add validation to ensure the fields are provided and are numbers.

---

#### **Part 4: Query Parameters**

1. Create a route `/filter` that accepts a query parameter `keyword` and returns a JSON object containing the keyword and its length.
   - Example: `/filter?keyword=flask` → `{"keyword": "flask", "length": 5}`

---

#### **Part 5: Structuring Responses**

1. Refactor all routes to include a `status` field in their responses.
   - Example: `{"status": "success", "data": {"sum": 12}}`

---

#### **Bonus Challenges 🌟**

1. Add a route `/factorial/<int:num>` that returns the factorial of `num`.
2. Modify `/sum` to handle lists of numbers instead of just two fields.

---

**Expected Output:**

- A Flask application with well-structured, RESTful endpoints.
- Validation for input data and query parameters.
- Consistent JSON responses for all routes.

---
