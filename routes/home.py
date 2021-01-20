from flask import request, render_template
from models.User import *
from __init__ import app
from services.AccountRepository import AccountManager as account
import flask
from DTOs.UserDTO import UserDTO
from services.access import require_access, ACCESS_LEVELS


@app.route('/home', methods=['POST', 'GET'])
@require_access(ACCESS_LEVELS['not_logged'])
def home():
    if request.method == 'POST':
        userDto= UserDTO(t=request.form['token'])
        userDto.u = account.decode_token(userDto.token)
        return render_template('home.html', username=userDto.u, token = userDto.token)
    return render_template('home.html')

