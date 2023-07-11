from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/one_to_many_relationship'

db = SQLAlchemy(app)
"""one-to-many relationship from roles to users because one role belongs to many users and users have only one role"""


class Role(db.Model):
    # ...one Role belongs to many users
    users = db.relationship('User', backref='role')


class User(db.model):
    # ...users have only one role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

# on the above code to get the user associated with a certain role
# user = User.query.get(1) this will get the user with an id of 1
# to get the role associated with the user with an id of 1 do the following
# role = user.role

# The users relationship on the Role model defines a one-to-many relationship between Roles and Users.This means that a Role can have many Users, but a User can only have one Role.
# The role_id column on the User model defines a foreign key that references the id column on the Role table.This means that the role_id value on a User must be the id of a Role in the Roles table.
# The role attribute on the User model is a property that refers to the Role associated with the User.This property is created by the backref parameter in the Role model.
# So to get the Role associated with a User
# user = User.query.get(1)
# role = user.role
