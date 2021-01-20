from models.User import *
from functools import wraps
from flask import request, flash, redirect
from DTOs.UserDTO import UserDTO
from services.AccountRepository import AccountManager as account
from __init__ import app

ACCESS_LEVELS = {
    'not_logged' : 0,
    'logged' : 1
}

def require_access(access_level):
    def up_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'token' in request.form:
                token = request.form['token']
                if access_level == 0:
                    if not token or not account.decode_token(token):
                        print("User not logged")
                        return redirect('/')
                if access_level == 1:
                    if token and account.decode_token(token):
                        print("User already logged on")
                        return redirect('/')
            else:
                return redirect('/')
            return func(*args, **kwargs)
        return wrapper
    return up_wrapper