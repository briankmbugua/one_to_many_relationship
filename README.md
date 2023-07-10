# One-to-Many Database Relationships with Flask-SQLAlchemy
A one-to-many database relationship is a relationship between two database tables where a record in one table can reference several records in another table.
# Example
In a blogging application a table for storing posts can have a one-to-many relationship with a table for storing comments.Each post can reference many comments, and each comment references a single post.Therefore one post has a relationship with many comments.The post table is a parent table, while the comments table is a child table -- a record in the parent table can reference many records in the child table.
# A small blogging system
to demonstrate one-to-many relationship i'll build a small blogging system that demonstrates how to build one-to-many relationship using the Flask-SQLAlchemy extension.You'll create a relationship between posts and comments, where each blog post can have several comments.