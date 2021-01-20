from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from __init__ import db
from models import User, Thread

class Reply(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    userCreatorID = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    threadRefferedID = db.Column(db.Integer, db.ForeignKey(Thread.id), nullable=False)
    content = db.Column(db.String, nullable=False)
    timestampEdited = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
