from flask import request, render_template, url_for, redirect
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify
from services.access import require_access, ACCESS_LEVELS
import os

@app.route('/u/<username>', methods=['POST', 'GET'])
# All access levels possible
def profile_info(username):
    user = User.query.filter_by(username=username).first()
    isRequestOwner = False
    logged=False
    if request.method == 'POST':
        token = request.form['token']
        client=account.get_user_by_token(token)
        if client:
            logged=True
        isRequestOwner = client.username == username

    return render_template('profile.html', user = user,logged=logged, isRequestOwner = isRequestOwner)


@app.route('/u/<username>/edit', methods=['POST', 'GET'])
@require_access(ACCESS_LEVELS['logged'])
def edit_profile_info(username):
    user = User.query.filter_by(username=username).first()
    isRequestOwner = False
    if request.method == 'POST':
        if len(request.form) > 1:
            first_name = request.form['first_name']
            print(first_name)
        token = request.form['token']
        isRequestOwner = account.get_user_by_token(token).username == username
        return render_template('edit_profile.html', user = user)
    if isRequestOwner == False:
        return redirect('/home')
    