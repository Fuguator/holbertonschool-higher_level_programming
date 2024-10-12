#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}
# write this script in the new terminal to add new user:
# curl -X POST http://localhost:5000/add_user -H "Content-Type: application/json" -d '{"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}'

@app.route("/")
def hello_world():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    username = list(users)
    return jsonify(username)

@app.route("/users/<username>", methods=['GET'])
def user_info(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/status")
def get_status():
    return 'OK', 200

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.json
    if data is None or data.get('username') is None:
        return jsonify({'error': 'Username is required'}), 400
    new_user = {
        'username': data.get('username'),
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[new_user.get('username')] = new_user
    return jsonify({'message': 'User added', 'user': new_user}), 201

if __name__ == "__main__":
    app.run()
