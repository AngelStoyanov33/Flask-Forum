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


@app.route('/reply/add', methods=['GET', 'POST'])
@require_access(ACCESS_LEVELS['logged'])
@requires_role(ROLES['user'])
def add_reply():
    if request.method == 'POST':

        token = request.form['token']
        user = account.get_user_by_token(token)

        threadRefferedID = request.form['threadRefferedID']
        content = request.form['reply_content']

        new_replydto = ReplyDTO(userCreatorID = user.id, threadRefferedID = threadRefferedID, content = content)
        created_replydto = replyService.addReply(new_replydto)

        if created_replydto != None:
            return jsonify(content=created_replydto.content, userCreator=user.username)
        else:
            return jsonify(content="", error="Adding thread in database failed")
    return "1"