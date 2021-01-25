from __init__ import app
import json
import appsettings
from models.Topic import *
from models.Thread import *
from services.Topic import TopicService as topicService
from flask.json import jsonify

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

    @staticmethod
    def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    @staticmethod
    def get_results_from_search(filter):
        #if not ThreadService.isUnique(topicdto): return None
        #topicID, title, content

        results = list()
        filter_topic_name = ThreadService.find_between(filter, "{", "}")
        
        if len(filter_topic_name)>0:
            filter_topic_id = topicService.get_topic_id_by_name(filter_topic_name)
            keyword=filter[filter.find('}')+1:].strip()
            for result in Thread.query.filter_by(topicID=filter_topic_id).filter(Thread.title.contains(keyword)):
                    results.append({
                        "id": result.id, 
                        "userCreatorID": result.userCreatorID, 
                        "topicID": result.topicID,
                        "title": result.title, 
                        "content": result.content,
                        "roleRequired": result.roleRequired, 
                        "timestampCreated": result.timestampCreated,
                        "timestampLastUpdated": result.timestampLastUpdated})
        else:
            keyword=filter.strip()
            for result in Thread.query.filter(Thread.title.contains(keyword)):
                results.append({
                    "id": result.id, 
                    "userCreatorID": result.userCreatorID, 
                    "topicID": result.topicID,
                    "title": result.title, 
                    "content": result.content,
                    "roleRequired": result.roleRequired, 
                    "timestampCreated": result.timestampCreated,
                    "timestampLastUpdated": result.timestampLastUpdated})
        return jsonify(results=results)


