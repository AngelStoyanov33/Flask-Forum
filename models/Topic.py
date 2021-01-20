from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from __init__ import db

class Topic(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    popularity = db.Column(db.Integer,nullable=False, default=0)
    db.UniqueConstraint(name)
