from flask import request, render_template, url_for, redirect
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify
from services.access import require_access, ACCESS_LEVELS
from services.upload import allowed_file
from werkzeug.utils import secure_filename
import os

@app.route('/process', methods=['POST', 'GET'])
def process_data():
    if request.method == 'POST':
        token = request.form['token']
        user = account.get_user_by_token(token)

        username = user.username

        user = User.query.filter_by(username=username).first()

        first_name = request.form['first_name']
        if first_name != "":
            user.firstName = first_name
        last_name = request.form['last_name']
        if last_name != "":
            user.lastName = last_name
        email = request.form['email']
        if email != "":
            user.email = email
        password = request.form['password']
        if password != "":
            user.password = account.hashPassword(password)
            
        if 'file' in request.args:
            file = request.files['file']
            if file and file.filename != "" and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], user.profilePicture))
                user.profilePicture = filename
        else:
            print("File not uploaded")

        db.session.commit()
        #TODO: password2 and password_conf

        

        return jsonify({'token': ""})