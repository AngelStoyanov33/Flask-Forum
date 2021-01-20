import hashlib
from models.User import *
from DTOs.UserDTO import UserDTO
from datetime import datetime
from itsdangerous import (
        TimedJSONWebSignatureSerializer as TJWSerializer,
        BadSignature,
        SignatureExpired
        )
from __init__ import app
import json
import appsettings

class AccountManager:
    def __init__(self):
        print("AM works!")

    @staticmethod
    def hashPassword(password):
        return hashlib.sha512(password.encode('utf-8')).hexdigest()

    @staticmethod
    def registerUser(userdto):
        passwordHash = AccountManager.hashPassword(userdto.password)
        #TODO SALT
        try:
            user= User(username = userdto.username, passwordHash = passwordHash, email = userdto.email)
            db.session.add(user)
            db.session.commit()
            
        except:
            return None
        return userdto

    @staticmethod
    def verify_password(password, user):
        return user.passwordHash == AccountManager.hashPassword(password)
    
    @staticmethod
    def generate_token(username):
        s = TJWSerializer(app.secret_key, expires_in = appsettings.expireTime)
        return s.dumps({'username': username}).decode('ascii')

    @staticmethod
    def decode_token(token):
        s = TJWSerializer(app.secret_key)
        return str((s.loads(token))).encode().decode('ascii')