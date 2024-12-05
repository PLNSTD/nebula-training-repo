### Topic 2: Building Simple Web Applications 🧑‍💻

#### Lecture: **Building RESTful APIs with Flask 📡**

**Objective:** Learn how to create RESTful APIs using Flask, focusing on serving and accepting JSON data, handling POST requests, and structuring API responses.

---

### **1. Introduction to RESTful APIs 🌐**

REST (Representational State Transfer) is an architectural style for designing networked applications. Flask makes it straightforward to build RESTful APIs.

Key Concepts:

- **Endpoints:** Routes that handle specific operations.
- **JSON:** The primary data format used for communication.
- **HTTP Methods:** Standard operations like GET, POST, PUT, and DELETE.

---

### **2. Serving JSON Data 📦**

Flask provides `jsonify` for returning JSON responses.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    return jsonify({"message": "Hello, World!"})
```

---

### **3. Handling POST Requests 📨**

Accepting JSON data:

```python
from flask import request

@app.route('/api/echo', methods=['POST'])
def echo():
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400

    message = request.json.get('message', None)
    if not message:
        return jsonify({"error": "Missing 'message' field"}), 400

    return jsonify({"echo": message})
```

Key Steps:

1. Check if the request contains JSON.
2. Validate required fields.
3. Return a response based on the data.

---

### **4. Structuring API Responses 🛠️**

Designing consistent responses improves usability. Include `status`, `data`, and `error` fields.

#### **Success Response Example**

```python
@app.route('/success')
def success():
    return jsonify({"status": "success", "data": {"message": "Operation successful"}}), 200
```

#### **Error Response Example**

```python
@app.route('/error')
def error():
    return jsonify({"status": "error", "error": {"code": 400, "message": "Bad Request"}}), 400
```

---

### **5. Adding Query Parameters 🔍**

Flask can handle query parameters via `request.args`.

Example:

```python
@app.route('/search')
def search():
    query = request.args.get('q', 'default')
    return jsonify({"search_query": query})
```

Access the endpoint like this:

```
http://127.0.0.1:5000/search?q=flask
```

---
