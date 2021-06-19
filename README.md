# Python Rest Api with Redis DB


Rest api Application with specific functionality.

## Features

- publish:  publish new messages to the REDIS server using a REST API POST request
- getLast:  retrieve the last message that was on the REDIS server using a REST API GET request
- getByTime: retrieve all messages that were on the REDIS and occurred between two given timestamps using a REST API GET request.


## Tech

- [Flask]   - used for rest api request
- [python]  - used in backend
- [Docker]  - containers 
- [Rides]   - DataBase
- [Postman] - to send GET/POST request 

## Usage
Application usage format

```json
{
    "publish":  {
                "command":"POST" ,
                "url format":"127.0.0.1:5000/publish/<Message>"
                },
    "getLast": {
                "command":"GET" ,
                "url format":"127.0.0.1:5000/getLast"
                },
    "getByTime":{
                "command":"GET" ,
                "url format":"127.0.0.1:5000/getByTime/YYYY-MM-DD HH-MM-SS/YYYY-MM-DD HH-MM-SS"
                }
}
```

## Functionality
**publish**
response example
-   message inserted to Redis : 
    `OK`

-   failed to insert message to Redis : 
    `failed to insert to redis`

**getLast**
Response example 
```json
{
    "Message": "Hello World!",
    "Recived at": "2021-06-19 13:03:16"
}
```
-   In case DB is empty we will got 
`"We still didn't recive any message"`

**getByDate**
Get request example via postman
```sh
127.0.0.1:5000/getByTime/2021-06-19 13:55:00/2021-06-19 14:06:00
```
Response example
```json
{
    "1": {
        "Message": "Hello World!",
        "Recived at": "2021-06-19 13:55:11"
    },
    "2": {
        "Message": "Hi",
        "Recived at": "2021-06-19 14:01:59"
    }
}
```

## Redis
**Data**
The messages saved in `sorted sets` 

```json
{
    "score":"insert date in epoch format",
    "message content": "<message><score>"
}
```
Save message
```sh
ZADD setName_key SCORE1 VALUE1
```

Retrive message by date  
```sh
ZRANGEBYSCORE setName_key start_date end_date [WITHSCORES] 
```
Retrive last message 
```sh
ZRANGE setName_key -1 -1 [WITHSCORES]
```
