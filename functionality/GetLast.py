from functionality.Base import Base

class GetLast(Base):
    def __init__(self):
        super().__init__()
        pass
    
    def get (self):
        lastMessage=self.redisDB.zrange(self.setName, '-1' ,'-1',withscores=True)
        if not lastMessage:
            return ("We still didn't recive any message")
        else:
            return self.parseMessage(lastMessage[0])
    