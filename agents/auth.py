import logging

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__)
login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    roles = db.Column(db.String(150), nullable=False)

    def has_role(self, role):
        return role in self.roles.split(",")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            logging.info(f"User {username} logged in successfully")
            return redirect(url_for("index"))
        flash("Invalid credentials")
        logging.warning("Invalid login attempt")
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    logging.info("User logged out successfully")
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=["GET", "POST"])
@limiter.limit("3 per hour")
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("auth.register"))
        hashed_password = generate_password_hash(password, method="sha256")
        new_user = User(username=username, password=hashed_password, roles="user")
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully")
        logging.info(f"New user registered: {username}")
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth.route("/admin")
@login_required
def admin():
    if not current_user.has_role("admin"):
        logging.warning(
            f"User {current_user.username} unauthorized access attempt to admin page"
        )
        flash("You do not have permission to view this page")
        return redirect(url_for("index"))
    return render_template("admin.html")