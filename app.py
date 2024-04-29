# app.py
from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/generate_password', methods=['GET'])
def generate_password():
    length = request.args.get('length', default=12, type=int)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
