from datetime import datetime
from functionality.Base import Base
message_dict={}
class GetByTime(Base):
    def __init__(self):
        super().__init__()
        pass
    
    def get (self,start,end):
        startEpoch=self.dateToEpoch(start)
        endEpoch=self.dateToEpoch(end)
        messages=self.redisDB.zrangebyscore(self.setName,startEpoch,endEpoch, withscores=True)
        return self.parseMessages (messages)


    def dateToEpoch(self,date):
        try:
            date=datetime.strptime(date, self.dateformat)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")
        return int(datetime.timestamp(date))

    def parseMessages(self,messages):
        index=0
        for message in messages:
            message=self.parseMessage(message)
            index+=1
            message_dict[index]=message
        return message_dict