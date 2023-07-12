# One-to-Many
```Python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'
```
# Explanation
## Models
- Post model 
- Comment model.
## Post model
Post model is the post table
- id -- the post ID.It is an Integer and a primary_key thus it will have a unique value assinged by the database for each entry that is each post
- title -- The post's title, A string with a maximum length of 100 characters
- content -- The post's content, db.Text indicates the column holds long texts.
### Explanation
- The comments class attribute defines a One-to-Many relationship between the Post model and the Comment model.
- You use the db.releationship() method, passing it the name of the comments model(Comment in this case)
- You use the backref parameter to add a back reference that behaves like a column to the Comment model.
- This way you can acces the post the comment was posted on using a post attribute.For Example, if you have a comment object in a variable called comment,You will be able to acces the post the comment belongs to using the ```comment.post```.
# __repr__
the __  __repr__ __ function allows you to give each object a string representation to recognize it for debugging purposes.