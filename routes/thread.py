from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from services.Thread import ThreadService as thread
import flask
from DTOs.UserDTO import UserDTO
from DTOs.TopicDTO import TopicDTO
from DTOs.ThreadDTO import ThreadDTO
from services.access import require_access, ACCESS_LEVELS
import json
from flask.json import jsonify
 

@app.route('/thread/add', methods=['POST'])
#@require_access(ACCESS_LEVELS['logged'])
def addThread():
        
    token = request.form['token']
    user = account.get_user_by_token(token)
    print(user.id)
        
    if user:
        threaddto=ThreadDTO(userCreatorID= user.id, title=request.form["threadName"], content=request.form["threadContent"], topicID=request.form["topicId"])
        new_thread = thread.createThread(threaddto=threaddto)
        if new_thread:
            return jsonify(title=new_thread.title, content=new_thread.content, userCreator=user.username)
        else:
            return jsonify(title="", content="", error="Adding thread in database failed")
    else:
        return jsonify(title="", content="", error="Unauthorized")

@app.route('/thread/delete/<id>', methods=['POST'])
def deleteThread(id):
    token = request.form['token']
    user = account.get_user_by_token(token)
    if user:
        threaddto=ThreadDTO( userCreatorID= user.id, title=request.form["threadName"], content=request.form["threadContent"], topicID=request.form["topicId"])
        new_thread = thread.createThread(threaddto=threaddto)
        if new_thread:
            return jsonify(title=new_thread.title, content=new_thread.content, userCreator=user.username)
        else:
            return jsonify(title="", content="", error="Adding thread in database failed")
    else:
        return jsonify(title="", content="", error="Unauthorized")