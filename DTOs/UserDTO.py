class UserDTO:
    username = str
    email = str
    password = str
    token = str
    def __init__(self, u="", e="", p="", t=""):
        self.username=u
        self.email=e
        self.password=p
        self.token=t
    