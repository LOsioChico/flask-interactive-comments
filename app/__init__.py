from flask import Flask
from app.utils import populate_db
from app.db.sqlalchemy import db
from app.views import comments_bp


def create_app():
    app = Flask(__name__)

    # Default config
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(comments_bp, url_prefix='/')

    with app.app_context():
        # Create Database Models
        db.create_all()
        # Populate the database if empty
        populate_db()

    return app
