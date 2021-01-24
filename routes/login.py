from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #data = json.loads(request.data.decode('ascii'))
        #username = data['username']
        #password = data['password']
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if not user or not account.verify_password(password, user):
            return jsonify({'token': None})
        userdto=UserDTO(username=username, password=password)
        user.token = account.generate_token(userdto)
        userdto=UserDTO(username=user.username, token=user.token)
        return jsonify(token=userdto.token, username=userdto.username)