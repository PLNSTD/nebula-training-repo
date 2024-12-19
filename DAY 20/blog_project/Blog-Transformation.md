Below is the updated assignment with the bonus challenges consolidated into a single optional task: creating a seed function to populate the database with dummy data every time the app is started (after dropping and recreating the table).

---

## Assignment: **Upgrading Your Flask Blog API with PostgreSQL 🎉**

### Overview

You previously built a simple blog backend using Flask and a Python dictionary. Now that you know how to integrate Flask with PostgreSQL via `psycopg2`, let’s upgrade your API to use a real database!

**Goal:** Transform your dictionary-based blog API into one that uses PostgreSQL for all CRUD operations.

---

### Learning Outcomes

- Connect a Flask application to a PostgreSQL database using `psycopg2`.
- Implement database initialization and schema creation for a `posts` table.
- Refactor CRUD endpoints to read and write data to the database rather than an in-memory dictionary.

---

### Prerequisites

- **Existing Code:** Your `blog.py` (or similar) from the previous blog assignment.
- **Database Knowledge:** Familiarity with creating and connecting to a PostgreSQL database.
- **psycopg2 Knowledge:** Basic `SELECT`, `INSERT`, `UPDATE`, `DELETE` queries from Python.

**Required Packages:**

```bash
pip install flask psycopg2-binary
```

---

### Step-by-Step Instructions

#### 1. Database Setup

1. **Create a Database:**
   Use `psql` or another tool to create a new database for your blog application:

   ```sql
   CREATE DATABASE blogdb;
   ```

2. **Connection Parameters:**
   In `blog.py`, set up your database connection details:
   ```python
   DATABASE = {
       'dbname': 'blogdb',
       'user': 'yourusername',
       'password': 'yourpassword',
       'host': 'localhost',
       'port': '5432'
   }
   ```

#### 2. Database Initialization

Implement a function to initialize your database and create a `posts` table:

```python
import psycopg2

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS posts;")
    cur.execute("""
        CREATE TABLE posts (
            post_id SERIAL PRIMARY KEY,
            username VARCHAR(50),
            title VARCHAR(100),
            content TEXT,
            date_created TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
```

You can call `initialize_db()` at the bottom of your script in debug mode or as a separate setup step before running the app.

#### 3. Refactor Your Endpoints

Refactor each of your existing endpoints (`GET /posts`, `POST /posts`, `GET /posts/<int:id>`, `PUT /posts/<int:id>`, `DELETE /posts/<int:id>`) to interact with the `posts` table using SQL queries. Reference your old code to understand the logic, but now replace dictionary operations with database queries.

**Example (GET /posts only):**

```python
@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT post_id, username, title, content, date_created FROM posts;")
    results = cur.fetchall()
    cur.close()
    conn.close()

    posts = []
    for row in results:
        posts.append({
            "post_id": row[0],
            "username": row[1],
            "title": row[2],
            "content": row[3],
            "date_created": str(row[4])
        })

    return {"status": "success", "data": posts}, 200
```

For the other endpoints, you should:

- Use `INSERT` to create a post.
- Use `SELECT` with a `WHERE` clause to get a specific post.
- Use `UPDATE` with a `WHERE` clause to modify an existing post.
- Use `DELETE` with a `WHERE` clause to remove a post.

---

### Testing & Validation

1. **Initialize Your Database:**
   At the bottom of your `blog.py`:

   ```python
   if __name__ == '__main__':
       initialize_db()
       app.run(debug=True)
   ```

2. **Run Your Application:**

   ```bash
   python blog.py
   ```

3. **Test Your Endpoints:**
   Use `curl`, Postman, or another HTTP client to:
   - `POST /posts` to create a post.
   - `GET /posts` to retrieve all posts.
   - `GET /posts/<int:id>` to retrieve a specific post.
   - `PUT /posts/<int:id>` to update a post.
   - `DELETE /posts/<int:id>` to delete a post.

---

### Bonus Challenge 🌟

**Seed Your Database with Dummy Data:**  
Create a `seed_db()` function that, after `initialize_db()`, inserts a few dummy posts into the `posts` table. This will give you some initial data on each run without having to manually create posts every time.

For example:

```python
def seed_db():
    conn = get_db_connection()
    cur = conn.cursor()
    dummy_posts = [
        ("alice", "First Post", "This is a seeded post!"),
        ("bob", "Another Post", "This post was inserted on startup."),
        ("charlie", "Welcome!", "Seeding the database makes testing easier.")
    ]
    for username, title, content in dummy_posts:
        cur.execute("INSERT INTO posts (username, title, content) VALUES (%s, %s, %s);", (username, title, content))
    conn.commit()
    cur.close()
    conn.close()
```

Call `seed_db()` right after `initialize_db()` in your `if __name__ == '__main__':` block:

```python
if __name__ == '__main__':
    initialize_db()
    seed_db()  # Populate the database with dummy data
    app.run(debug=True)
```

Now, every time you restart the application, your table is dropped, recreated, and pre-populated with some initial data.

---

### Submission

- Submit your updated `blog.py` (and any additional files if you created them).
- Include a short `README.md` explaining how to set up and run your application, including instructions for database initialization.
- Provide sample requests (like `curl` commands) in your README or code comments to help verify the endpoints.

**By completing this assignment, you’ll have successfully migrated from an in-memory data store to a fully-fledged PostgreSQL-backed API and will have automated initial data seeding for ease of testing. Good luck!**
