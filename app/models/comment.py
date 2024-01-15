from app.db.sqlalchemy import db


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='comments', lazy=True)
    replies = db.relationship('Reply', backref='comment', lazy=True)

    def __init__(self, content, created_at, score, user_id):
        self.content = content
        self.created_at = created_at
        self.score = score
        self.user_id = user_id

    def __repr__(self):
        return f'<Comment {self.content}>'
