from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome To my Project BackEnd!"}

# Part 1
@app.route('/status')
def status():
    return {"status": "OK!"}

# Part 2
@app.route('/square/<int:number>')
def square(number):
    return {"result": number ** 2}

# Part 3
@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    # Part 4.2 and BonusChallenge.2
    if not data or 'message' not in data:
        # abort(400)
        return bad_request(), 400
    return {'echo': data['message']}

# Part 4.2
@app.errorhandler(400)
def bad_request(error=None):
    return {'error': "Bad Request... Make sure your post request follows this pattern {'message': 'Hello'}"}

# Part 4.1
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Resource not found!'}

# Part 5
@app.route('/add/<int:a>/<int:b>')
def sum(a, b):
    return {'result': a + b}

if __name__ == '__main__':
    app.run(debug=True)