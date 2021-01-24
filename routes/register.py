
from flask import request, render_template
from models.User import *
from __init__ import app

from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify
from services.Account import AccountManager as account


@app.route('/register', methods=['POST', 'GET'])

def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        userdto=UserDTO(username=username, email=email, password=password)
        new_user = account.registerUser(userdto=userdto)
        #user.token = account.generate_token(user.username)
        #userdto=UserDTO(username=user.username, token=user.token)
        #return jsonify(token=userdto.token, username=userdto.username)
        if new_user:
            new_user.token = account.generate_token(new_user)
            return jsonify(token=new_user.token, username=new_user.username)
        else:
            return jsonify(token="", username="", error="Registration in database failed")

    return render_template('register.html')
