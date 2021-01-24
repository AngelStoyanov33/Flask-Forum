
from flask import request, render_template
from models.User import *
from __init__ import app
from services.Account import AccountManager as account
import flask

@app.route('/', methods=['POST', 'GET'])
def welcome():
    registerMode=False
    if flask.request.method=="POST":
        try:
            register_mode = int(request.form.get("registerMode"))
            if register_mode>0:
                registerMode=True
        except:
            pass
    return render_template('index.html',registerMode=registerMode)

