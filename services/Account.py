import hashlib
from models.User import *
from DTOs.UserDTO import UserDTO
from datetime import datetime
from itsdangerous import (
        TimedJSONWebSignatureSerializer as TJWSerializer,
        BadSignature,
        SignatureExpired
        )
import json
import appsettings

class AccountManager:
    def __init__(self):
        print("AM works!")

    @staticmethod
    def hashPassword(password):
        return hashlib.sha512(password.encode('utf-8')).hexdigest()

    @staticmethod
    def is_unique(userdto):
        user = User.query.filter_by(username=userdto.username).first()
        if not user:
            return True
        return False

    @staticmethod
    def registerUser(userdto):
        passwordHash = AccountManager.hashPassword(userdto.password)
        #TODO SALT
        if not AccountManager.is_unique(userdto = userdto): return None
        
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
    def generate_token(userdto):
        s = TJWSerializer(appsettings.secret_key, expires_in = appsettings.expire_time)
        return s.dumps({'username': userdto.username}).decode('ascii')

    @staticmethod
    def decode_token(token):
        s = TJWSerializer(appsettings.secret_key)
        return str((s.loads(token))).encode().decode('ascii')

    @staticmethod
    def get_user_by_token(token):
        if token:
            s = TJWSerializer(appsettings.secret_key)
            payload = s.loads(token)
            return User.query.filter_by(username=payload.get('username')).first()
        else:
            return None

    @staticmethod
    def get_user_by_id(id):
        return User.query.filter_by(id=id).first()        

    @staticmethod
    def check_permission(user, role):
        return True if user.role >= role else False    