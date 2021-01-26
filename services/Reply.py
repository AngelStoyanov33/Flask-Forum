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
    def editReply(reply_id, content):
        try:
            reply = Reply.query.filter_by(id = reply_id).first()
            reply.content = content

            db.session.commit()
        except:
            return None

        return reply_id

    @staticmethod
    def deleteReply(reply_id):
        try:
            Reply.query.filter_by(id = reply_id).delete()
            db.session.commit()
        except:
            return None

        return reply_id