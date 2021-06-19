import datetime
from functionality.Base import Base
import time

redisInsertStatus = {
  0: "failed to insert to redis",
  1: "OK"
}

class Publish(Base):
    def __init__(self):
        super().__init__()
        pass


    def post(self,message):
        epochTime=int(time.time()) # in case we have a lot of publish(post) request here. we can use the decimal dot also with number of the message (auto increment)
        message=message.strip()
        dateStr=datetime.datetime.fromtimestamp(epochTime).strftime(self.dateformat)

        result=self.redisDB.zadd(self.setName, {message+dateStr:epochTime})
        print  (redisInsertStatus[result])
        return (redisInsertStatus[result])
        
