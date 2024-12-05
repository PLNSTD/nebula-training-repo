from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"status": "API is running"})

@app.route('/reverse/<string:text>')
def reverse_text(text):
    return jsonify({"reversed": text[::-1]})

@app.route('/sum', methods=['POST'])
def sum():
    if not request.json:
        return bad_request("Request must be JSON"), 400
    
    message = request.json
    if not message.get('a', None) or not message.get('b', None):
        return bad_request("Message must contain 'a' and 'b' as keys"), 400
    
@app.errorhandler(400)
def bad_request(error_msg):
    return jsonify({"error": error_msg})


if __name__ == '__main__':
    app.run(debug=True)