from app.db.sqlalchemy import db
from app.models import User, Comment, Reply


def populate_db():
    """Populate the database with some dummy entries."""
    if db.session.query(User).count() == 0:
        users = [
            User(username="juliusomo",
                 image="https://randomuser.me/api/portraits/men/3.jpg"),
            User(username="amyrobson",
                 image="https://randomuser.me/api/portraits/women/2.jpg"),
            User(username="maxblagun",
                 image="https://randomuser.me/api/portraits/men/1.jpg"),
            User(username="ramsesmiron",
                 image="https://randomuser.me/api/portraits/men/4.jpg"),
        ]

        # pylint: disable=line-too-long
        comments = [
            Comment(content="Impressive! Though it seems the drag feature could be improved. But overall it looks incredible. You've nailed the design and the responsiveness at various breakpoints works really well.",
                    created_at="1 month ago",
                    score=12,
                    user_id=2),
            Comment(content="Woah, your project looks awesome! How long have you been coding for? I'm still new, but think I want to dive into React as well soon. Perhaps you can give me an insight on where I can learn React? Thanks!",
                    created_at="2 weeks ago",
                    score=5,
                    user_id=3),
        ]

        replies = [
            Reply(content="If you're still new, I'd recommend focusing on the fundamentals of HTML, CSS, and JS before considering React. It's very tempting to jump ahead but lay a solid foundation first.",
                  created_at="1 week ago",
                  score=4,
                  replying_to=2,
                  user_id=4,
                  comment_id=2),
            Reply(content="I couldn't agree more with this. Everything moves so fast and it always seems like everyone knows the newest library/framework. But the fundamentals are what stay constant.",
                  created_at="2 days ago",
                  score=2,
                  replying_to=4,
                  user_id=1,
                  comment_id=2)
        ]

        for user in users:
            db.session.add(user)

        for comment in comments:
            db.session.add(comment)

        for reply in replies:
            db.session.add(reply)

        db.session.commit()
