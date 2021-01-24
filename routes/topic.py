from flask import request
from models.Topic import *
from __init__ import app
from services.Account import AccountManager as account
from services.Topic import TopicService as topicService
import flask
from DTOs.UserDTO import UserDTO
from DTOs.TopicDTO import TopicDTO
from services.access import require_access, ACCESS_LEVELS
import json
from flask.json import jsonify


@app.route('/topic/add', methods=['POST', 'GET'])
#@require_access(ACCESS_LEVELS['logged'])
def addTopic():
    if request.method == 'POST':
        topicdto=TopicDTO(name=request.form["topicName"], popularity=0)

        new_topic = topicService.createTopic(topicdto=topicdto)
        if new_topic:
            return jsonify(name=new_topic.name, popularity=new_topic.popularity)
        else:
            return jsonify(name="", popularity=0, error="Adding topic in database failed")
    return "1"


