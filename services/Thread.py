from __init__ import app
import json
import appsettings
from models.Topic import *
from models.Thread import *

class ThreadService:
    def __init__(self):
        print("TS works!")

    @staticmethod
    def createThread(threaddto, user):
        #if not ThreadService.isUnique(topicdto): return None

        try:
            thread= Thread(userCreatorID= user.id, title = threaddto.title, content=threaddto.content, topicID= threaddto.topicID)
            db.session.add(thread)
            db.session.commit()
            
        except:
            return None
        return threaddto

