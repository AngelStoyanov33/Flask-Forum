class ReplyDTO:
    userCreatorID = int
    threadRefferedID= int
    content = str

    def __init__(self, userCreatorID=0, threadRefferedID=0, content=""):
        self.userCreatorID = userCreatorID
        self.threadRefferedID = threadRefferedID
        self.content = content