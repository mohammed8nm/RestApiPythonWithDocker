import datetime
from os import replace
from flask_restful import Resource
import redis


class Base(Resource):
    def __init__(self):
        print("Init Base and DB")
        self.redisDB=redis.Redis()
        self.setName='messages'
        self.dateformat='%Y-%m-%d %H:%M:%S'

    def get (self):
        return "Get request is not supported for this url"

    def post(self):
        return "Post request is not supported for this url"
    
    def parseMessage(self,messagesAndScores):
        returnMessages={'Message':'{}',
                'Recived at':'{}'}
        messagewithepoch=messagesAndScores[0].decode('UTF-8')
        epochTime=int(messagesAndScores[1])
        dateStr=datetime.datetime.fromtimestamp(epochTime).strftime(self.dateformat)
        message=(messagewithepoch[::-1].replace(dateStr[::-1],'', 1))[::-1]
        returnMessages['Message']=message
        returnMessages['Recived at']=dateStr
        return returnMessages