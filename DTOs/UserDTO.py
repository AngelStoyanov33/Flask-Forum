class UserDTO:
    username = str
    email = str
    password = str
    token = str
    role = int
    def __init__(self, username="", email="", password="", token="", role=0):
        self.username=username
        self.email=email
        self.password=password
        self.token=token
        self.role=role