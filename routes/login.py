from flask import request, render_template
from models.User import *
from __init__ import app
from services.AccountRepository import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #data = json.loads(request.data.decode('ascii'))
        #username = data['username']
        #password = data['password']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=email).first()
        if not user or not account.verify_password(password, user):
            return jsonify({'token': None})
        #token = user.generate_token()
        user.token = account.generate_token(user.username)
        userdto=UserDTO(u=user.username, t=user.token)
        return jsonify(token=userdto.token, username=userdto.username)