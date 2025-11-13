from flask import Blueprint, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
bcrypt = Bcrypt()

auth_bp = Blueprint('auth', __name__)

USERS = {
    "maxwell@poop.com": bcrypt.generate_password_hash("password123").decode("utf-8")
}

class User(UserMixin):
    def __init__(self, email):
        self.id = email

@login_manager.user_loader
def load_user(email):
    if email in USERS:
        return User(email)
    return None

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email, password = data.get("email"), data.get("password")
    if not email or not password:
        return jsonify({"message": "Missing credentials"}), 400
    
    if email in USERS and bcrypt.check_password_hash(USERS[email], password):
        login_user(User(email))
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Login Failed"}), 401

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})

@auth_bp.route("/whoami")
@login_required
def whoami():
    return jsonify({"user": current_user.id})