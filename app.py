from functionality.Base import Base
from functionality.GetLast import GetLast
from functionality.GetByTime import GetByTime
from functionality.Publish import Publish
from logging import debug
from flask import Flask
from flask_restful import Api

app =Flask (__name__)
api=Api(app)
base=Base()
#cache = redis.Redis(host='redis', port=6379)

usage ={
    '/publish':{'description':'publish new messages to the REDIS server using a REST API POST request',
                'format':'127.0.0.1:5000/publish/<Message>',
                'example':'127.0.0.1:5000/publish/a s'},
    '/getLast':{'description':'retrieve the last message that was on the REDIS server',
                'format':'127.0.0.1:5000/getLast',
                'example':'127.0.0.1:5000/getLast'},
    '/getByTime':{'description':'retrieve all messages that were on the REDIS and occurred between two given timestamps',
                'format':'127.0.0.1:5000/getByTime/YYYY-MM-DD HH-MM-SS/YYYY-MM-DD HH-MM-SS',
                'example':'127.0.0.1:5000/getByTime/2021-06-19 14:55:11/2021-06-29 14:56:11'}
}

@app.route('/')
def appUsage():
    return (usage)
      
api.add_resource(GetByTime, '/getByTime/<string:start>/<string:end>')
api.add_resource(GetLast, '/getLast')
api.add_resource(Publish, '/publish/<string:message>')

if __name__ == "__main__":
    app.run(debug=True)
    
