class ReplyDTO:
    id = int
    userCreatorID = int
    threadRefferedID= int
    content = str

    def __init__(self, id = 0, userCreatorID=0, threadRefferedID=0, content=""):
        self.id = id
        self.userCreatorID = userCreatorID
        self.threadRefferedID = threadRefferedID
        self.content = content