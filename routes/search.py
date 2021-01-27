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


@app.route('/search', methods=['POST', 'GET'])
#@require_access(ACCESS_LEVELS['not_logged'])
def search():
    if request.method == 'POST':
        addTopicMode= False
        addThreadMode= False
        logged = True
        token = request.form['token']
        search = request.form['search']
        
        client= accountService.get_user_by_token(token)
        if not client:
            client=UserDTO(username="guest")
            logged=False

        results = list()
        results = threadService.get_results_from_search(search)
        return render_template('search.html', client= client, results=results, search=search, logged=logged)