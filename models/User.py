from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from __init__ import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwordHash = db.Column(db.String, nullable=False)
    profilePicture = db.Column(db.String, nullable=False, default = "DEFAULT")
    role = db.Column(db.Integer, nullable=False, default = 1)
    firstName = db.Column(db.String, nullable=True, default = "Not specified")
    lastName = db.Column(db.String, nullable=True, default = "Not specified")
    timestampRegister = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestampLastOnline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    db.UniqueConstraint(username, email)
