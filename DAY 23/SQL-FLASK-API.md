# 🐍 Python Database Interactions with `psycopg2` and Flask API

Welcome to the session on integrating Python applications with PostgreSQL using `psycopg2` and building a RESTful API with Flask. This lecture will guide you through setting up a Flask API to perform CRUD operations on a PostgreSQL database.

## 🎯 Learning Outcomes

By the end of this session, you'll be able to:

- Establish connections to PostgreSQL databases using `psycopg2` in Python.
- Create a RESTful API with Flask to perform CRUD operations.
- Execute SQL commands from Python applications to interact with databases.
- Apply best practices for database interaction, including managing connections and transactions.

## 🔧 Prerequisites

Ensure you have the necessary packages installed:

```bash
pip install flask psycopg2-binary
```

## 🛠️ Setting Up the Flask Application

### 🏗️ Step 1: Create the Flask App

Create a file called `app.py` with the following content:

```python
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection parameters
DATABASE = {
    'dbname': 'yourdbname',
    'user': 'yourusername',
    'password': 'yourpassword',
    'host': 'yourhost',
    'port': 'yourport'
}

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    return "Welcome to the Flask API with psycopg2!"
```

### 📋 Step 2: GET - Retrieve Data

Define a route to retrieve data from the `users` table:

```python
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)
```

### 🔍 Step 3: GET by ID - Retrieve Data

Define a route to retrieve a specific user by their ID:

```python
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users WHERE id = %s LIMIT 1', (id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(user) if user else ('User not found', 404)
```

### ➕ Step 4: POST - Insert Data

Define a route to insert data into the `users` table:

```python
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    name = new_user['name']
    email = new_user['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_user), 201
```

### ✏️ Step 5: PUT - Update Data

Define a route to update data in the `users` table:

```python
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    updated_user = request.get_json()
    name = updated_user['name']
    email = updated_user['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(updated_user)
```

### 🗑️ Step 6: DELETE - Delete Data

Define a route to delete data from the `users` table:

```python
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204
```

### 🚀 Step 7: Running the Flask Application

To run your Flask application, add the following code to the bottom of your `app.py` file:

```python
if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
```

Run your application by executing:

```bash
python app.py
```

You now have a Flask API that initializes the database by dropping the existing `users` table (if it exists) and creating a new one, and can perform CRUD operations on a PostgreSQL database using `psycopg2`.

## 📚 Conclusion

Building a RESTful API with Flask and `psycopg2` allows for powerful and flexible database interactions within your applications. By following the steps and best practices outlined in this lecture, you'll be able to perform essential CRUD operations and manage your database connections effectively.

Practice these concepts, experiment with different SQL queries, and you'll gain confidence in handling database interactions in your Python projects.

## 📖 Additional Resources

- **[psycopg2 Documentation](https://www.psycopg.org/docs/)**
- **[PostgreSQL Official Documentation](https://www.postgresql.org/docs/)**
- **[Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)**

Feel free to explore these resources to deepen your understanding and enhance your skills in database interactions with Python and Flask.
