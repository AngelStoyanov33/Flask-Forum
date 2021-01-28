from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from services.Reply import ReplyService as replyService
import flask
from DTOs.UserDTO import UserDTO
from DTOs.ThreadDTO import ThreadDTO
from DTOs.ReplyDTO import ReplyDTO
from services.access import require_access, requires_role, ACCESS_LEVELS, ROLES
import json
from flask.json import jsonify


@app.route('/thread/<thread_id>/reply/add', methods=['GET', 'POST'])
@require_access(ACCESS_LEVELS['logged'])
@requires_role(ROLES['user'])
def add_reply(thread_id):
    if request.method == 'POST':

        token = request.form['token']
        user = account.get_user_by_token(token)

        content = request.form['reply_content']

        new_replydto = ReplyDTO(userCreatorID = user.id, threadRefferedID = thread_id, content = content)
        created_replydto = replyService.addReply(new_replydto)

        if created_replydto != None:
            return jsonify(content=created_replydto.content, userCreator=user.username, status="Success")
        else:
            return jsonify(content="", status="Adding reply in database failed")
    return "1"


@app.route('/thread/<thread_id>/reply/<reply_id>/edit', methods=['GET', 'POST'])
# @require_access(ACCESS_LEVELS['logged'])
# @requires_role(ROLES['user'])

def edit_reply(thread_id, reply_id):
    if request.method == 'POST':

        token = request.form['token']
        user = account.get_user_by_token(token)

        content = request.form['reply_content']

        new_replydto = ReplyDTO(id = reply_id, userCreatorID = user.id, threadRefferedID = thread_id, content = content)
        edited_replydto = replyService.editReply(new_replydto)

        if edited_replydto != None:
            print("SUCESS")
            return jsonify(content=edited_replydto.content, userCreator=user.username, status="Success")
        else:
            print("NO SUCESS")
            return jsonify(content="", status="Editing reply failed")
    return "1"

@app.route('/thread/<thread_id>/reply/<reply_id>/delete', methods=['POST'])
def delete_reply(thread_id, reply_id):
    token = request.form['token']
    user = account.get_user_by_token(token)

    replydto = ReplyDTO(id=reply_id)
    deleted_reply = replyService.deleteReply(replydto)

    if deleted_reply:
        return jsonify(status="Success")
    else:
        return jsonify(status="Error")