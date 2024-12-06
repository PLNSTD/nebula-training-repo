from flask import Flask, jsonify, request

app = Flask(__name__)

db = {
    'current_post_id': 0,
    'posts': {}
}

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
    
# 1. GET /posts
@app.route('/posts')
def get_posts():
    return success({'posts': db['posts']})

# 2. POST /posts
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json

    if 'title' not in new_post or 'content' not in new_post:
        return bad_request('Bad request title or content not in json request')

    db['current_post_id'] += 1
    new_post['post_id'] = db['current_post_id']
    db['posts'][new_post['post_id']] = new_post

    return success(new_post)

# 3. GET Post by ID
@app.route('/posts/<int:id>')
def get_post_by_id(id):
    if id not in db['posts']:
        return jsonify({'error': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
