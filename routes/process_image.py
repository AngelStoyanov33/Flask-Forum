from flask import request, render_template, url_for, redirect
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
from DTOs.UserDTO import UserDTO
import json
from flask.json import jsonify
from services.access import require_access, ACCESS_LEVELS
from services.upload import allowed_file, random_string
from werkzeug.utils import secure_filename
import os

@app.route('/process/image', methods=['POST', 'GET'])
def process_image():
    if request.method == 'POST':
        token = request.form['token']
        user = account.get_user_by_token(token)

        username = user.username

        user = User.query.filter_by(username=username).first()
            
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != "" and allowed_file(file.filename):
                file.filename = secure_filename(file.filename)
                file_extension = os.path.splitext(file.filename)[1]
                file.filename = random_string(10)
                file.filename = file.filename + "." + file_extension
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                # if user.profilePicture != "DEFAULT":
                #     os.remove(os.path.join(app.config['UPLOAD_FOLDER'], user.profilePicture))
                user.profilePicture = file.filename
        else:
            print("File not uploaded")

        db.session.commit()
        #TODO: password2 and password_conf

        return jsonify(token="")