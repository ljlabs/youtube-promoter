""" This acts as the applications main entry point.

When the application is installed using `python setup.py install/develop` the
application will be accessible by running `python -m template`.
"""
from youtube_promoter.handler.taskHandler import TaskHandler
import json

if __name__ == "__main__":
    with open('config.json', 'r+') as file:
        config = json.loads(file.read())
        th = TaskHandler(config=config)
        for task in th.getTasks():
            task.process()
