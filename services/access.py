from models.User import *
from functools import wraps
from flask import request, flash, redirect
from DTOs.UserDTO import UserDTO
from services.Account import AccountManager as account
from __init__ import app
import json

ACCESS_LEVELS = {
    'not_logged' : 0,
    'logged' : 1,
    'moderator': 2
}

def require_access(access_level):
    def up_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'token' in request.form:
                token = request.form['token']
                #if access_level == 0:
                    #if not token or not account.decode_token(token):
                    #    print("User not logged")
                    #    return redirect('/')
                if access_level == 1:
                    if not token and account.decode_token(token):
                        print("User already logged on")
                        return redirect('/')
                if access_level == 2:
                    accountDetails= {}
                    if len(token)==0:
                         print("Guest has no permission for that")
                         return redirect('/')

                    payload = account.decode_token(token)
                    accountDetails = json.loads(payload.replace('\'',"\""))
                    user = User.query.filter_by(username=accountDetails['username']).first()
                    if user.role=="User":
                        print("User has no permission for that")
                        return redirect('/')
            else:
                return redirect('/')
            return func(*args, **kwargs)
        return wrapper
    return up_wrapper