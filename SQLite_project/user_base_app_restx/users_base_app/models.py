from users_base_app import db
from users_base_app.config import *


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(LONG_STRING_SIZE), nullable=False)
    salt = db.Column(db.String(LONG_STRING_SIZE), nullable=False)
