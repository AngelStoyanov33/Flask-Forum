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
        
        token = request.form['token']
        account_details= {}
        if len(token)>0:
            payload = accountService.decode_token(token)
            account_details = json.loads(payload.replace('\'',"\""))
        else:
            account_details['username']='guest'
        userDto= UserDTO(username=account_details['username'], token=request.form['token'])
        topics = topicService.getAll()
        try:
            topic_mode = int(request.form.get("addTopicMode"))
            thread_mode = int(request.form.get("addThreadMode"))
            print("A")
            topics = topicService.getAll()
            print(topics)
            if topic_mode>0:
                addTopicMode=True
                
            if thread_mode>0:
                addThreadMode=True
                
                topics = topicService.getAll()
                return render_template('home.html', username=userDto.username, token = userDto.token, addTopicMode=addTopicMode, addThreadMode=addThreadMode, topics=topics["topics"])
        except:
            pass

        return render_template('home.html', username=userDto.username, token = userDto.token, addTopicMode=addTopicMode, addThreadMode=addThreadMode, topics=topics["topics"])

