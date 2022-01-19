from extentions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, Primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__