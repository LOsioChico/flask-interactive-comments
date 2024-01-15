from app.db.sqlalchemy import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image = db.Column(db.String(50))

    def __init__(self, username, image):
        self.username = username
        self.image = image

    def __repr__(self):
        return f'<User {self.username}>'
