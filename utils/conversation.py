class Conversation:
    def __init__(self):
        self.conversation = {}
        self.responseOn = 0
    def addResponse(self, response):
        self.conversation[self.responseOn] = response
        self.responseOn += 1
    def getConversation(self):
        return self.conversation

