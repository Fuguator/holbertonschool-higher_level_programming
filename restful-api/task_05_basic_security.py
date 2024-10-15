#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-puper-very-complicated-key"
jwt = JWTManager(app)
auth = HTTPBasicAuth()



users = {
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"},
    "regular_user": {"password": generate_password_hash("userpass"), "role": "user"}
}



@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None



@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"



@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
         #access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401



@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def func():
    return "JWT Auth: Access Granted"



@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user_identity = get_jwt_identity()
    if user_identity['role'] == 'admin':
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403



@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401



@jwt.invalid_token_loader
def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401



@jwt.expired_token_loader
def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401



@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401



@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401



if __name__ == '__main__':
    app.run()
