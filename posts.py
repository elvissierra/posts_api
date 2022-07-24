from settings import *
import json

db = SQLAlchemy(app)


class Posts(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def json(self):
        return {"id": self.id, "title": self.title, "genre": self.genre}

    def add_post(title, genre):
        new_post = Posts(title=title, genre=genre)
        db.session.add(new_post)
        db.session.commit()

    def get_all_posts():
        return [Posts.json(posts) for posts in Posts.query.all()]

    def get_post(id):
        return [Posts.json(Posts.query.filter_by(id=id).first())]

    def update_post(id, title, genre):
        post_to_update = Posts.query.filter_by(id=id).first()
        post_to_update.title = title
        post_to_update.genre = genre
        db.session.commit()

    def delete_post(id):
        Posts.query.filter_by(id=id).delete
        db.session.commit()
