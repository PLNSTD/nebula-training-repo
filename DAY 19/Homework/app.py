from flask import Flask, request, jsonify

app = Flask(__name__)

# Part 1
@app.route('/status')
def status():
    return success({"status": "API is running"})

# Part 2
@app.route('/reverse/<string:text>')
def reverse_text(text):
    return success({"reversed": text[::-1]})

# Part 3 and Bonus Challenge 2
@app.route('/sum', methods=['POST'])
def sum_route():
    if not request.json:
        return bad_request("Request must be JSON"), 400
    
    message = request.json

    # Bonus Challenge 2
    if not message.get('nums', None):
        return bad_request("Message must contain 'nums' field")
    
    if not isinstance(message['nums'], list):
        return bad_request("Nums field must contain a list of numbers")
    
    return success({'sum': sum(message['nums'])})

    # Part 3
    # if not message.get('a', None) or not message.get('b', None):
    #     return bad_request("Message must contain 'a' and 'b' as keys"), 400
    
    # return success({"sum": message['a'] + message['b']})

# Part 4
@app.route('/filter')
def filter():
    query = request.args.get('keyword', 'default')

    return success({"keyword": query, "length": len(query)})

# Part 5
# Refactor all routes to include a status field in their responses
@app.route('/success')
def success(data):    
    return jsonify({"status": "success", "data": data}), 200

# Bonus Challenge 1
@app.route('/factorial/<int:input_num>')
def factorial(input_num):
    if input_num < 0:
        return bad_request('Factorial is not defined for negative numbers')
    
    result = 1
    for num in range(input_num, 0, -1):
        result *= num

    return success({'factorial': result})

@app.errorhandler(400)
def bad_request(error_msg):
    return jsonify({"error": error_msg}), 400

if __name__ == '__main__':
    app.run(debug=True)