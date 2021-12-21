from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# company project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50))
    app_type = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# company user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    scope = db.relationship('Project')


# personal project
class p_Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50))
    app_type = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('p_user.id'))

# personal user
class p_User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    scope = db.relationship('p_Project')