class ThreadDTO:
    id = int
    userCreatorID = int
    topicID= int
    title = str
    content = str
    roleRequired = int
    def __init__(self, id=0, userCreatorID=0, topicID=0, title="", content="", roleRequired=0):
        self.id = id
        self.userCreatorID=userCreatorID
        self.topicID=topicID
        self.title=title
        self.content=content
        self.roleRequired=roleRequired