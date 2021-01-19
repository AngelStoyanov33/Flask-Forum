
from flask import request, render_template
from models.User import *
from __init__ import app
from services.AccountRepository import AccountManager as account
import flask
from DTOs.UserDTO import UserDTO

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        userDto= UserDTO(t=request.form['token'])
        userDto.u = account.decode_token(userDto.t)

    return render_template('home.html', username=userDto.u, token =  userDto.t)

