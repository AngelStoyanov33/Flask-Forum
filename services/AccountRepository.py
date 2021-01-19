import hashlib
from models.User import *
from DTOs.UserDTO import UserDTO
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
            user= User(username=userdto.username, passwordHash=passwordHash, email=userdto.email)
            db.session.add(user)
            db.session.commit()
            
        except:
            return None
        return userdto

    @staticmethod
    def verify_password(password, user):
        return user.passwordHash == AccountManager.hashPassword(password)
    

        