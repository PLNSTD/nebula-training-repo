from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

db = {
    'current_post_id': 0,
    'posts': {}
}

if os.path.exists('db.json'):
    with open('db.json', 'r') as file:
        db = json.load(file)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Blog API!"})

# Success request
@app.route('/success')
def success(data):
    return jsonify({"status": "sucess", "data": data}), 200

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
    
    posts = []

    if query_title != 'default':
        for key, value in db['posts'].items():
            if query_title in value['title']:
                posts.append(value)

    if query_content != 'default':
        for key, value in db['posts'].items():
            if query_content in value['content']:
                posts.append(value)

    if query_content == 'default' and query_title == 'default':
        posts = list(db['posts'].values())
    
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

    save_db()

    return success(new_post)

# 3. GET Post by ID
@app.route('/posts/<int:id>')
def get_post_by_id(id):
    if id not in db['posts']:
        return not_found('Post Not Found!')

    target_post = db['posts'].get(id)
    return success(target_post) 
    
# 4. PUT Update a Post
@app.route("/posts/<int:id>", methods=['PUT'])
def update_post(id):
    if id not in db['posts']:
        return not_found("No id found")
    
    updated_post = request.json

    if 'title' in updated_post:
        db['posts'].get(id)['title'] = updated_post['title']
    if 'content' in updated_post:
        db['posts'].get(id)['content'] = updated_post['content']
    
    save_db()

    return success(db['posts'].get(id))

# 5. DELETE a Post
@app.route("/posts/<int:id>", methods=['DELETE'])
def delete_posts(id):
    if id not in db['posts']:
        return not_found("No Id Found")
    
    db['posts'].pop(id, None)
    save_db()

    return success('Post Deleted')


# Extra Challenge - Data Persistence
def save_db():
    with open('db.json', 'w') as file:
        json.dump(db, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
