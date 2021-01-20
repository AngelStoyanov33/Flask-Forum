class UserDTO:
    username = str
    email = str
    password = str
    token = str
    def __init__(self, username="", email="", password="", token=""):
        self.username=username
        self.email=email
        self.password=password
        self.token=token
    