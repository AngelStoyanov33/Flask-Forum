from flask import request, render_template
from models.User import *
from __init__ import app
from services.AccountRepository import AccountManager as account
import flask
from DTOs.UserDTO import UserDTO
from services.access import require_access, ACCESS_LEVELS
import json


@app.route('/home', methods=['POST', 'GET'])
@require_access(ACCESS_LEVELS['not_logged'])
def home():
    if request.method == 'POST':
        token = request.form['token']
        accountDetails= {}
        if(len(token)>0):
            payload = account.decode_token(token)
            accountDetails = json.loads(payload.replace('\'',"\""))
        else:
            accountDetails['username']='guest'
        userDto= UserDTO(username=accountDetails['username'], token=request.form['token'])
        
        return render_template('home.html', username=userDto.username, token = userDto.token)

