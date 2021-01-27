from __init__ import app
import json
import appsettings
from models.Reply import *
from flask import jsonify


class ReplyService:
    @staticmethod
    def addReply(replydto):
        try:
            new_reply = Reply(userCreatorID = replydto.userCreatorID, threadRefferedID = replydto.threadRefferedID, content = replydto.content)
            db.session.add(new_reply)
            db.session.commit()
        except:
            return None

        return replydto

    @staticmethod
    def editReply(replydto):
        try:
            if replydto.content != "":
                reply = Reply.query.filter_by(id = replydto.id).first()
                reply.content = replydto.content
                db.session.commit()
        except:
            return None

        return replydto

    @staticmethod
    def deleteReply(replydto):
        try:
            Reply.query.filter_by(id = replydto.id).delete()
            db.session.commit()
        except:
            return None

        return replydto


    @staticmethod
    def get_all_replies(threaddto):
        try:
            replies = Reply.query.filter_by(threadRefferedID = threaddto.id).all()
        except:
            return None

        return replies