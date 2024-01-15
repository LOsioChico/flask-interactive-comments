from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.utils import populate_db
from app.db.sqlalchemy import db


def create_app():
    app = Flask(__name__)

    # Default config
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        # Create Database Models
        db.create_all()
        # Populate the database if empty
        populate_db()

    return app
