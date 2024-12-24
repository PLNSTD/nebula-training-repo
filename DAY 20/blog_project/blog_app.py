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
    

def execute_query(query, params=None, fetch=None):
    conn = None
    try:
        conn = psycopg2.connect(**DATABASE)
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch == 'one':
                return cur.fetchone()
            elif fetch == 'all':
                return cur.fetchall()
            else:
                conn.commit()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        if conn:
            if cur:
                cur.close()
            conn.close()

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
    
    '''conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM posts;")
    results = cur.fetchall()
    cur.close()
    conn.close()'''

    results = execute_query('SELECT id, title, content FROM posts;', fetch='all')
    print(results)
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

    '''conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (title, content) VALUES (%s, %s);', (new_post['title'], new_post['content']))
    conn.commit()
    cur.close()
    conn.close()'''

    execute_query('INSERT INTO posts (title, content) VALUES (%s, %s);', params=(new_post['title'], new_post['content']))

    # save_db()

    return success(new_post)

# 3. GET Post by ID
@app.route('/posts/<int:id>')
def get_post_by_id(id):

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s;", (id,))
    results = cur.fetchone()
    cur.close()
    conn.close()

    if not results:
        return not_found('Post not found!')

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
    updated_post = request.json

    conn = get_db_connection()
    cur = conn.cursor()
    if 'title' in updated_post:
        # db['posts'].get(str(id))['title'] = updated_post['title']
        cur.execute('UPDATE posts SET title = %s WHERE id = %s', (updated_post['title'], id)) # TRY execute_query LAST LINEEEEEEEEEE
    if 'content' in updated_post:
        # db['posts'].get(str(id))['content'] = updated_post['content']
        cur.execute('UPDATE posts SET content = %s WHERE id = %s', (updated_post['content'], id)) # TRY execute_query LAST LINEEEEEEEEEE
    # results = cur.fetchall()
    rows_affected = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()

    # print(results)

    '''if not results:
        return not_found('Post not found!')'''
    
    # save_db()

    # return success(db['posts'].get(str(id)))
    if rows_affected == 0:
        return bad_request('No rows were updated')
    else:
        return success(updated_post)

# 5. DELETE a Post
@app.route("/posts/<int:id>", methods=['DELETE'])
def delete_posts(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM posts WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()

    return '', 204
    # DB as JSON
    '''if str(id) not in db['posts']:
        return not_found("No Id Found")
    
    db['posts'].pop(str(id), None)
    save_db()

    return success('Post Deleted')'''

# Extra Challenge - Data Persistence
def save_db():
    with open('db.json', 'w') as file:
        json.dump(db, file, indent=4)

if __name__ == '__main__':
    # initialize_db()
    app.run(debug=True)


'''
# Utility function to simplify query execution
def execute_query(query, params=None, fetch=None):
    """
    Executes an SQL query with optional parameters and fetch behavior.
    Args:
        query (str): SQL query to execute.
        params (tuple or list): Query parameters.
        fetch (str): Fetch mode - 'one', 'all', or None.
    Returns:
        list or dict: Query results if fetch='one' or 'all', otherwise None.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DATABASE)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            if fetch == 'one':
                return cur.fetchone()
            elif fetch == 'all':
                return cur.fetchall()
            else:
                conn.commit()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        if conn:
            conn.close()
 
'''