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


@app.route('/addThread', methods=['POST', 'GET'])
#@require_access(ACCESS_LEVELS['logged'])
def addThread():
    if request.method == 'POST':
        threaddto=ThreadDTO(title=request.form["threadName"], content=request.form["threadContent"], topicID=request.form["topicId"])
        print("a")
        token = request.form['token']
        payload = account.decode_token(token)
        account_details = json.loads(payload.replace('\'',"\""))

        user = User.query.filter_by(username=account_details['username']).first()

        new_thread = thread.createThread(threaddto=threaddto, user=user)
        if new_thread:
            return jsonify(title=new_thread.title, content=new_thread.content, userCreator=user.username)
        else:
            return jsonify(natitleme="", content="", error="Adding thread in database failed")
    return "1"

