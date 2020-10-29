import xml.etree.ElementTree as XML
import os
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


def subscribe(queryParameters):
    try:
        mode = queryParameters['hub.mode']
        challenge = queryParameters['hub.challenge']
        verify_token = queryParameters['hub.verify_token']
    except KeyError:
        return {'statusCode': 404, 'body': ''}

    if mode == 'subscribe' and verify_token == secret:
        return {'statusCode': 200, 'body': challenge}
    return {'statusCode': 404, 'body': ''}


def handleUpdate(bodyParams):
    root = XML.fromstring(bodyParams)

    for entry in root.findall('xmlns:entry', namespaces=namespaces):
        video = parse_video_params(entry)
        config = json.loads(os.environ.get('config'))
        th = TaskHandler(config=config)
        for task in th.getTasks():
            task.process(video)
    return {'statusCode': 404, 'body': 'Goodly'}
