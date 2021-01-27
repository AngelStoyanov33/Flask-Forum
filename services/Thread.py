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
    def createThread(threaddto):
        #if not ThreadService.isUnique(topicdto): return None

        try:
            print(threaddto.userCreatorID)
            thread= Thread(userCreatorID= threaddto.userCreatorID, title = threaddto.title, content=threaddto.content, topicID= threaddto.topicID)
            db.session.add(thread)
            db.session.commit()
        except:
            return None
        return threaddto

    @staticmethod
    def delete_thread(id, user):
        #if not ThreadService.isUnique(topicdto): return None
        thread = ThreadService.get_thread_by_id(id)
        if thread.userCreatorID==user.id or user.role>1:
            try:
                Thread.query.filter_by(id = id).delete()
                db.session.commit()
            except:
                return None
        else:
            return None
        return id

    @staticmethod
    def edit_thread(threaddto, user):

        thread = ThreadService.get_thread_by_id(threaddto.id)
        if thread.userCreatorID==user.id or user.role>1:
            try:
                if threaddto.title != "":
                    thread.title = threaddto.title
                if threaddto.content != "":
                    thread.content = threaddto.content
                    db.session.commit()
            except:
                return None
        else:
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
    def get_thread_by_id(id):
        return Thread.query.filter_by(id=id).first()


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
                        "timestampCreated": str(result.timestampCreated)[:10],
                        "timestampLastUpdated": str(result.timestampLastUpdated)[:10]})
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
                    "timestampCreated": str(result.timestampCreated)[:10],
                    "timestampLastUpdated": str(result.timestampLastUpdated)[:10]})
        return results


