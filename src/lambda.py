from youtube_promoter.services.pubsubhubhub import subscribe, handleUpdate
import json
import os


def lambda_handler(event, context):
    config = json.loads(os.environ.get('config'))
    if event["httpMethod"] == "GET":
        return subscribe(event["queryStringParameters"], config)
    elif event["httpMethod"] == "POST":
        return handleUpdate(event["body"], config)
    return {'statusCode': 405, 'body': ''}
