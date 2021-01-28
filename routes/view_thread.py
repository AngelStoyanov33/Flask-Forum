from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as accountService
from services.Topic import TopicService as topicService
from services.Thread import ThreadService as threadService
from services.Reply import ReplyService as replyService
import flask
from DTOs.UserDTO import UserDTO
from DTOs.ThreadDTO import ThreadDTO
from services.access import require_access, ACCESS_LEVELS
import json


@app.route('/thread/<id>', methods=['POST', 'GET'])
#@require_access(ACCESS_LEVELS['not_logged'])
def view_thread(id):
    

    #TODOS
    # add ed buttons if user is creator
    # make page accessable for guests if no role required
    editReplyMode = False
    editMode = False
    reply_to_be_edited_id = -1


    if "threadEditMode" in request.form:
        if int(request.form["threadEditMode"])>0:
            editMode=True

    if "editReplyMode" in request.form:
        if int(request.form["editReplyMode"]) > 0:
            editReplyMode = True

    if "replyId" in request.form:
        if int(request.form["replyId"]) > 0:
            reply_to_be_edited_id = int(request.form["replyId"])
            
        
    thread = threadService.get_thread_by_id(id)
    labelCreated = str(thread.timestampCreated)[:16]
    userCreator = accountService.get_user_by_id(thread.userCreatorID)
    logged = False
    client = UserDTO(username="guest")
    threaddto = ThreadDTO(id = id)

    replies_list = replyService.get_all_replies(threaddto)
    repliers = {}

    for reply in replies_list:
        repliers[reply] = accountService.get_user_by_id(reply.userCreatorID)

    if "token" in request.form:
        client = accountService.get_user_by_token(request.form['token'])
        
        if client:
            logged = True
            print(client.username)
            if 1<thread.roleRequired:
                return render_template("denied.html")

    print(editMode)
    return render_template('view_thread.html', reply_to_be_edited_id = reply_to_be_edited_id, id=id, thread=thread, labelCreated=labelCreated, userCreator=userCreator, client=client, logged=logged, editMode=editMode, editReplyMode = editReplyMode, replies = replies_list, repliers = repliers)
