from flask import Flask, jsonify, request
import json
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

db = {
    'current_post_id': 0,
    'posts': {}
}

DATABASE = {
    'dbname': 'blog_db',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def data_transfer_to_db():
    conn = get_db_connection()
    cur = conn.cursor()
    for key, post in db["posts"].items():
        cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s);", (post["title"], post["content"]))
    conn.commit()
    cur.close()
    conn.close()

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE IF EXISTS posts;
    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR(50),
        content VARCHAR(200)
    )
     """)
    # cur.execute("""INSERT INTO posts (title, content) VALUES ('Title3', 'My first DB post');""")
    conn.commit()
    cur.close()
    conn.close()
    data_transfer_to_db()

if os.path.exists('db.json'):
    with open('db.json', 'r') as file:
        db = json.load(file)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Blog API!"})

# Success request
@app.route('/success')
def success(data):
    return jsonify({"status": "success", "data": data}), 200

# Error handler
@app.errorhandler(400)
def bad_request(msg):
    return jsonify({'error': msg}), 400

# Not Found Handler
@app.errorhandler(404)
def not_found(msg):
    return jsonify({'error': msg}), 404
    
# 1. GET /posts
@app.route('/posts')
def get_posts():
    query_title = request.args.get('title', 'default')
    query_content = request.args.get('content', 'default')
    page = request.args.get('page', '1')  # Default to '1' if not provided
    page_size = request.args.get('size', '2')  # Default to '2' if not provided

    # Validate and convert page and size to integers
    try:
        query_page = int(page)
        query_page_size = int(page_size)
    except ValueError:
        return bad_request("'page' and 'size' must be valid integers.")
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM posts;")
    results = cur.fetchall()
    cur.close()
    conn.close()

    posts = []

    for row in results:
        posts.append({
            "post_id": row[0],
            "title": row[1],
            "content": row[2],
        })

    if query_title != 'default':
        print(query_title)
        for value in posts:
            if query_title in value['title']:
                posts.append(value)

    if query_content != 'default':
        print(query_content)
        for value in posts:
            if query_content in value['content']:
                posts.append(value)
    
    # Pagination
    # 0, 1, 2, 3, 4
    # page 3 size 2-> idx = 4 ... 6
    # page 1 -> start_idx = (page - 1) * size & end_idx = start_idx + size
    start_idx = (query_page - 1) * query_page_size
    end_idx = start_idx + query_page_size

    if end_idx > len(posts):
        end_idx = len(posts)
    if start_idx >= len(posts):
        start_idx = len(posts) - query_page_size
        end_idx = len(posts)
    posts = posts[start_idx: end_idx]

    return success({'posts': posts})

# 2. POST /posts
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json

    if 'title' not in new_post or 'content' not in new_post:
        return bad_request('Bad request title or content not in json request')

    db['current_post_id'] += 1
    new_post['post_id'] = db['current_post_id']
    db['posts'][new_post['post_id']] = new_post

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (title, content) VALUES (%s, %s);', (new_post['title'], new_post['content']))
    conn.commit()
    cur.close()
    conn.close()

    # save_db()

    return success(new_post)

# 3. GET Post by ID
@app.route('/posts/<int:id>')
def get_post_by_id(id):

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s;", (str(id)))
    results = cur.fetchone()
    cur.close()
    conn.close()

    post = {
        'id': results[0], 
        'title': results[1],
        'content': results[2]
    }

    # if str(id) not in db['posts']:
    #     print(db)
    #     return not_found('Post Not Found!')

    # target_post = db['posts'].get(str(id))
    return success(post)
    
# 4. PUT Update a Post
@app.route("/posts/<int:id>", methods=['PUT'])
def update_post(id):
    if str(id) not in db['posts']:
        return not_found("No id found")
    
    updated_post = request.json

    if 'title' in updated_post:
        db['posts'].get(str(id))['title'] = updated_post['title']
    if 'content' in updated_post:
        db['posts'].get(str(id))['content'] = updated_post['content']
    
    save_db()

    return success(db['posts'].get(str(id)))

# 5. DELETE a Post
@app.route("/posts/<int:id>", methods=['DELETE'])
def delete_posts(id):
    if str(id) not in db['posts']:
        return not_found("No Id Found")
    
    db['posts'].pop(str(id), None)
    save_db()

    return success('Post Deleted')

# Extra Challenge - Data Persistence
def save_db():
    with open('db.json', 'w') as file:
        json.dump(db, file, indent=4)

if __name__ == '__main__':
    # initialize_db()
    app.run(debug=True)
