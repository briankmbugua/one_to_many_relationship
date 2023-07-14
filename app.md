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

# Comment model
The Comment model represents the comment table.
- id: The comment ID. you define it as an integer with db.Integer.primary_key=True
- content: The comment's content. db.Text indicates the column holds long texts.
- post_id: An integer foreign key you construct using db.Foreignkey() class, which is a key that links a table with another, using that table's primary key.
- This links a comment to a post using the primary key of the post, which is its ID.
- The post table is a parent table, which indicates that each post has many comments.
- The comment table is a child table.
- Each comment is related to a parent post using the post's ID. Therefore, each comment has a post_id column that can be used to access the post the comment was posted on.