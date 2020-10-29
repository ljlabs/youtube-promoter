import xml.etree.ElementTree as XML
import json
from youtube_promoter.handler.taskHandler import TaskHandler

secret = 'some_url_safe_secret'
namespaces = {
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'xmlns': 'http://www.w3.org/2005/Atom'
}


def parse_video_params(entry):
    video_id = entry.find('yt:videoId', namespaces=namespaces).text
    title = entry.find('xmlns:title', namespaces=namespaces).text
    link = entry.find('xmlns:link', namespaces=namespaces).get('href')
    return {"video_id": video_id, "title": title, "link": link}


def subscribe(queryParameters, config):
    try:
        mode = queryParameters['hub.mode']
        challenge = queryParameters['hub.challenge']
        verify_token = queryParameters['hub.verify_token']
    except KeyError:
        return {'statusCode': 404, 'body': ''}

    if mode == 'subscribe' and verify_token == config["pubsubhubhub_secret"]:
        return {'statusCode': 200, 'body': challenge}
    return {'statusCode': 404, 'body': ''}


def handleUpdate(bodyParams, config):
    root = XML.fromstring(bodyParams)

    for entry in root.findall('xmlns:entry', namespaces=namespaces):
        video = parse_video_params(entry)
        th = TaskHandler(config=config)
        for task in th.getTasks():
            task.process(video)
    return {'statusCode': 404, 'body': 'Goodly'}
