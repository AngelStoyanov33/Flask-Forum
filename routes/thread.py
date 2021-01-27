from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as accountService
from services.Thread import ThreadService as threadService
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
    user = accountService.get_user_by_token(token)
    print(user.id)
        
    if user:
        threaddto=ThreadDTO(userCreatorID= user.id, title=request.form["threadName"], content=request.form["threadContent"], topicID=request.form["topicId"])
        new_thread = threadService.createThread(threaddto=threaddto)
        if new_thread:
            return jsonify(title=new_thread.title, content=new_thread.content, userCreator=user.username)
        else:
            return jsonify(title="", content="", error="Adding thread in database failed")
    else:
        return jsonify(title="", content="", error="Unauthorized")

@app.route('/thread/delete/<id>', methods=['POST'])
def deleteThread(id):
    token = request.form['token']
    user = accountService.get_user_by_token(token)
    deleted_id = threadService.delete_thread(id, user)
    if deleted_id:
        return jsonify(status="Success")
    else:
        return jsonify(status="Error")
        


@app.route('/thread/edit/<id>', methods=['POST'])
def editThread(id):
    token = request.form['token']
    user = accountService.get_user_by_token(token)

    threaddto = ThreadDTO(id=id,title=request.form["threadName"], content=request.form["threadContent"])
    threaddto = threadService.edit_thread(threaddto, user)
    if threaddto:
        return jsonify(title=threaddto.title, content=threaddto.content, status="Success")
    else:
        return jsonify(status="Error")

