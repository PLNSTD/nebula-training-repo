### Topic 1: Flask Basics - Lecture and Assignment

#### Lecture: **Flask Basics: Building a Backend 🛠️**

**Objective:** Lay the foundation for creating Flask backends by understanding routes, request handling, and response formatting.

---

### **1. Introduction to Flask 🚀**

Flask is a lightweight Python framework for building web backends. It’s minimal and lets you focus on the functionality without unnecessary overhead.

Key Features:

- Simple routing
- Built-in server
- Modular and extensible

Install Flask:

```bash
pip install flask
```

---

### **2. Starting a Flask App 🏗️**

1. Create a file `app.py`.
2. Import Flask and create an instance:

   ```python
   from flask import Flask
   app = Flask(__name__)
   ```

3. Add a basic route:

   ```python
   @app.route('/')
   def home():
       return {"message": "Welcome to Flask Backend!"}
   ```

4. Run the app:
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

Access your app at `http://127.0.0.1:5000`.

---

### **3. Routes and Request Methods 🔄**

Flask routes handle incoming HTTP requests.

#### **Example: Basic GET Route**

```python
@app.route('/hello')
def hello():
    return {"message": "Hello, World!"}
```

#### **Dynamic Routes**

Dynamic routes include variables:

```python
@app.route('/user/<username>')
def greet_user(username):
    return {"message": f"Hello, {username}!"}
```

#### **Handling POST Requests**

Flask makes it easy to handle different request methods:

```python
from flask import request

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return {"received": data}
```

---

### **4. Error Handling 🛑**

Flask provides decorators for custom error responses.

#### **Example: 404 Error**

```python
@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404
```

#### **Example: 500 Error**

```python
@app.errorhandler(500)
def server_error(error):
    return {"error": "Server error"}, 500
```
