class ThreadDTO:
    id = int
    userCreatorID = int
    topicID= int
    title = str
    content = str
    roleRequired = int
<<<<<<< HEAD
    def __init__(self, id=0, userCreatorID=0, topicID=0, title="", content="", roleRequired=0):
        self.id = id
        self.userCreatorID=userCreatorID
        self.topicID=topicID
        self.title=title
        self.content=content
        self.roleRequired=roleRequired
=======
    def __init__(self, userCreatorID=0, topicID=0, title="", content="", roleRequired=0):
        self.userCreatorID = userCreatorID
        self.topicID = topicID
        self.title = title
        self.content = content
        self.roleRequired = roleRequired
>>>>>>> 07cfc3220e74aee3ffe680d63b7c445a7151c0b3
