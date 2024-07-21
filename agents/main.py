import os
import sys

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

from auth import auth, db, login_manager
from logging_config import setup_logging
from task_scheduler import start_scheduler


def create_app():
    app = Flask(__name__)
    load_dotenv()
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///db.sqlite3"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE', 'filesystem')

    print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")
    print(f"SQLALCHEMY_DATABASE_URI: {os.getenv('DATABASE_URL')}")
    print(f"SESSION_TYPE: {os.getenv('SESSION_TYPE')}")

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    JWTManager(app)
    Session(app)
    CORS(app)
    Talisman(app)

    # Setup rate limiting
    limiter = Limiter(app, key_func=get_remote_address)

    # Register blueprints
    app.register_blueprint(auth, url_prefix="/auth")

    # Setup logging
    setup_logging()

    # Create database tables
    with app.app_context():
        db.create_all()

    # Start scheduler
    start_scheduler()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
