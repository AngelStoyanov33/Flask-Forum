from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as accountService
from services.Topic import TopicService as topicService
from services.Thread import ThreadService as threadService
import flask
from DTOs.UserDTO import UserDTO
from services.access import require_access, ACCESS_LEVELS
import json


@app.route('/thread/<id>', methods=['POST', 'GET'])
#@require_access(ACCESS_LEVELS['not_logged'])
def view_thread(id):
    
    token = request.form['token']

    thread = threadService.get_thread_by_id(id)
    userCreator = accountService.get_user_by_id(thread.userCreatorID)

    account_details= {}
    if len(token)>0:
        payload = accountService.decode_token(token)
        account_details = json.loads(payload.replace('\'',"\""))
    else:
        account_details['username']='guest'
    userDto = UserDTO(username=account_details['username'], token=request.form['token'])

    labelCreated = str(thread.timestampCreated)[:16]

    return render_template('view_thread.html', id=id, thread=thread, labelCreated=labelCreated, userCreator=userCreator)

