from youtube_promoter.services.pubsubhubhub import subscribe, handleUpdate
import json


def lambda_handler(event, context):
    if event["httpMethod"] == "GET":
        return subscribe(event["queryStringParameters"])
    elif event["httpMethod"] == "POST":
        return handleUpdate(event["body"])
    return {'statusCode': 405, 'body': ''}
