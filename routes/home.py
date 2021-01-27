from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as accountService
from services.Topic import TopicService as topicService
import flask
from DTOs.UserDTO import UserDTO
from services.access import require_access, ACCESS_LEVELS
import json


@app.route('/home', methods=['POST', 'GET'])
@require_access(ACCESS_LEVELS['not_logged'])
def home():
    if request.method == 'POST':
        addTopicMode= False
        addThreadMode= False
        logged = True
        token = request.form['token']
        client = accountService.get_user_by_token(token)
        if not client:
            client=UserDTO(username="guest")
            logged=False

        topics = topicService.getAll()
        try:
            topic_mode = int(request.form.get("addTopicMode"))
            thread_mode = int(request.form.get("addThreadMode"))

            topics = topicService.getAll()

            if topic_mode>0:
                addTopicMode=True
            if thread_mode>0:
                addThreadMode=True
                
                topics = topicService.getAll()
                return render_template('home.html', username=client.username, logged=logged, addTopicMode=addTopicMode, addThreadMode=addThreadMode, topics=topics["topics"])
        except:
            pass

        return render_template('home.html', username=client.username, logged=logged, addTopicMode=addTopicMode, addThreadMode=addThreadMode, topics=topics["topics"])

