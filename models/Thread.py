from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from __init__ import db
from models.User import *
from models.Topic import *


class Thread(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    userCreatorID = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    topicID= db.Column(db.Integer, db.ForeignKey(Topic.id))
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    roleRequired = db.Column(db.Integer, nullable=False, default = 0)
    timestampCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    timestampLastUpdated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
