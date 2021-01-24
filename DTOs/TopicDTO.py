class TopicDTO:
    name = str
    popularity = int
    def __init__(self, name="", popularity=0):
        self.name=name
        self.popularity=popularity
    