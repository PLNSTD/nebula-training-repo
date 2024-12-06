### Mini Project: **Building a Simple Blog Backend 📝**

#### Objective

Create a minimal blog backend using Flask. This project will involve setting up endpoints to:

- Create blog posts.
- Retrieve all posts.
- Retrieve a specific post by ID.
- Update a post.
- Delete a post.

You’ll use a Python dictionary to simulate a database. Follow the steps below to guide your progress.

---

### Step 1: Project Setup ⚙️

1. **Create a Virtual Environment:**

   - Navigate to your project folder in your terminal:
     ```bash
     mkdir flask_blog && cd flask_blog
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the environment:
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **Mac/Linux:**
       ```bash
       source venv/bin/activate
       ```

2. **Install Flask:**

   ```bash
   pip install flask
   ```

3. **Start a Flask App:**

   - Create a file `blog.py` and initialize your Flask app:
     ```python
     from flask import Flask
     app = Flask(__name__)
     ```
   - Add a basic route to verify your setup:
     ```python
     @app.route('/')
     def home():
         return {"message": "Welcome to the Blog API!"}
     ```
   - Run your app and visit `http://127.0.0.1:5000` in your browser to confirm it works:
     ```bash
     python blog.py
     ```

4. **Create a "Database":**
   - Define a Python dictionary to store blog posts and a variable to manage unique IDs:
     ```python
     posts = {}
     current_id = 1
     ```

---

### Step 2: Endpoints Overview 🛠️

You’ll create the following endpoints:

1. `GET /posts` – Retrieve all posts.
2. `POST /posts` – Create a new post.
3. `GET /posts/<int:id>` – Retrieve a specific post by ID.
4. `PUT /posts/<int:id>` – Update an existing post.
5. `DELETE /posts/<int:id>` – Delete a post.

Each will use JSON to handle requests and responses.

---

### Step 3: Build Endpoints (Your Turn 🔨)

1. **Retrieve All Posts:**

   - Create a `GET /posts` route that returns all blog posts.
   - Hint: Use `posts.values()` to get all posts.
   - Your response should look like:
     ```json
     { "status": "success", "data": [] }
     ```

2. **Create a New Post:**

   - Create a `POST /posts` route that:
     - Accepts JSON with `title` and `content`.
     - Validates that these fields exist.
     - Adds a new post to the `posts` dictionary.
     - Returns the newly created post.
   - Hint: Use the global `current_id` to assign unique IDs and increment it after each new post.

3. **Retrieve a Post by ID:**

   - Create a `GET /posts/<int:id>` route.
   - Return the post with the given ID, or a 404 error if it doesn’t exist.
   - Hint: Use `posts.get(id)` to retrieve the post.

4. **Update a Post:**

   - Create a `PUT /posts/<int:id>` route.
   - Allow the user to update the `title` or `content` of a post.
   - Return the updated post, or a 404 error if it doesn’t exist.
   - Hint: Use the `.get()` method on the incoming JSON data.

5. **Delete a Post:**
   - Create a `DELETE /posts/<int:id>` route.
   - Remove the post with the given ID from the dictionary.
   - Return a success message, or a 404 error if the post doesn’t exist.

---

### Step 4: Testing Your API 🧪

1. **Run Your App:**

   ```bash
   python blog.py
   ```

2. **Test Endpoints:**
   - Use **Postman**, **curl**, or your preferred tool to test each endpoint.
   - Example `curl` commands:
     - **Create a post:**
       ```bash
       curl -X POST http://127.0.0.1:5000/posts -H "Content-Type: application/json" -d '{"title": "My First Post", "content": "This is my first blog post!"}'
       ```
     - **Retrieve all posts:**
       ```bash
       curl http://127.0.0.1:5000/posts
       ```
     - **Retrieve a specific post:**
       ```bash
       curl http://127.0.0.1:5000/posts/1
       ```
     - **Update a post:**
       ```bash
       curl -X PUT http://127.0.0.1:5000/posts/1 -H "Content-Type: application/json" -d '{"title": "Updated Title"}'
       ```
     - **Delete a post:**
       ```bash
       curl -X DELETE http://127.0.0.1:5000/posts/1
       ```

---

### Step 5: Extra Challenges 🌟

1. **Search Posts:**

   - Add query parameters to the `GET /posts` route to filter posts by title.
   - Example: `/posts?title=blog`

2. **Pagination:**

   - Implement `page` and `size` parameters in the `GET /posts` route to return paginated results.

3. **Data Persistence:**
   - Modify your app to save posts to a file and load them when the app starts.

---
