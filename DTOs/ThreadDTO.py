class ThreadDTO:
    userCreatorID = int
    topicID= int
    title = str
    content = str
    roleRequired = int
    def __init__(self, userCreatorID=0, topicID=0, title="", content="", roleRequired=0):
        self.userCreatorID=userCreatorID
        self.topicID=topicID
        self.title=title
        self.content=content
        self.roleRequired=roleRequired