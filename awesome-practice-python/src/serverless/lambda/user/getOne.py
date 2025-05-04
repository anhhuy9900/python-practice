import json
import logging
import os


def handler(event, context):
    print('GetAll -handler - event: ', event)
    # data = json.loads(event['body'])
    item = {}
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
