from flask import Flask
import os

from config import Config
from extensions import db, login_manager


def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Login configuration
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login to continue."

    # Create upload directories
    os.makedirs(
        app.config["LOST_UPLOAD_FOLDER"],
        exist_ok=True
    )

    os.makedirs(
        app.config["FOUND_UPLOAD_FOLDER"],
        exist_ok=True
    )

    # Register blueprints
    from models.notifications import Notifications

    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.items import items_bp
    from routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(admin_bp)

    # Import models
    from models.user import User
    from models.item import Item
    from models.claim import Claim

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


# Create Flask application
app = create_app()


# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):

    from models.user import User

    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )