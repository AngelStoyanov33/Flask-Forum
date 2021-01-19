
from flask import request, render_template
from models.User import *
from __init__ import app
from services.AccountRepository import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        userdto=UserDTO(u=username, e=email, p=password)

        newUser = account.registerUser(userdto=userdto)
        
        if userdto:
            newUser.token = "a"
            return jsonify(token=newUser.token, username=newUser.username)
        else:
            return jsonify(token="", username="", error="Registration in database failed")

    return render_template('register.html')
