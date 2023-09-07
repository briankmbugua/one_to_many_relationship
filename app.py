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


# Displaying All Posts
# create a route and a template to display all the posts in the database on the index page

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


# Displaying a single Post and its Comments
# create a route to and template to display the details of each post on a dedicated page, and the post's comments below it.

@app.route('/<int:post_id>/', methods=('GET', 'POST'))
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment = Comment(content=request.form['content'], post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    return render_template('post.html', post=post)


# Displaying all comments
@app.route('/comments/')
def comments():
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template('comments.html', comments=comments)


# Deleting Comments
# add a delete comment button below each comment to allow users to delete unwanted comments

@app.post('/comments/<int:comment_id>/delete')
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True)
