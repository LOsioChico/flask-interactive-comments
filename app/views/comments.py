from flask import Blueprint, render_template
from app.models import Comment


comments_bp = Blueprint('comments', __name__)


@comments_bp.route('/', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)
