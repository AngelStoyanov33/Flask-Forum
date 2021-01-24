from __init__ import app
import json
import appsettings
from models.Topic import *
from models.Thread import *

class TopicService:
    def __init__(self):
        print("TS works!")

    @staticmethod
    def isUnique(topicdto):
        topic = Topic.query.filter_by(name=topicdto.name).first()
        if not topic:
            return True
        return False

    @staticmethod
    def createTopic(topicdto):
        #if not ThreadService.isUnique(topicdto): return None
        try:
            topic= Topic(name = topicdto.name, popularity=topicdto.popularity)
            db.session.add(topic)
            db.session.commit()
            print("Add")
        except:
            return None
            
        return topicdto
    
    @staticmethod
    def getAll():
        topics = Topic.query.all()
        topicsSerialized= list()
        for topic in  topics:
            topicsSerialized.append({"id": topic.id, "name": topic.name, "popularity": topic.popularity})
        output= {"topics":topicsSerialized}
        return output