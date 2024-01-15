from app.db.sqlalchemy import db


class Reply(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    replying_to = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='replies', lazy=True)
    comment_id = db.Column(db.Integer, db.ForeignKey(
        'comment.id'), nullable=False)

    def __init__(self, content, created_at, score, replying_to, user_id, comment_id):
        self.content = content
        self.created_at = created_at
        self.score = score
        self.replying_to = replying_to
        self.user_id = user_id
        self.comment_id = comment_id

    def __repr__(self):
        return f'<Reply {self.content}>'
