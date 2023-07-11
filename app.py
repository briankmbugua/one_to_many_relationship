from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/one_to_many_relationship'

db = SQLAlchemy(app)


# Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    # defines a One-to-Many relationship between the Post model and the Comment model
    # backref is used to create a back reference from the Comment model to the Post model
    # this means you can access the Post object from the Comment object by using the post attribute
    # if you have a Comment object, you can get the Post object like this
    # "comment = Comment.query.get(1)"
    # post = comment.post
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'


# Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "self.content[:20]...">'


"""The comments class attribute defines a One-to-Many relationship between the Post model and the Comment model.You use the db.relationship() method, passing it the name of the comments model(Comment in this case).You use the backref parameter to add a back reference that behaves like a column to the Comment model.This way, you can access the post the comment was posted on using a post attribute.
Example if there is a comment with an id of 1. then we can acces the Post associated with that Comment by doing the following.
comment = Comment.query.get(1) this is the comment
to get the post associated with the above comment
post = comment.post"""
