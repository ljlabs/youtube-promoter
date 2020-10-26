import json

import click

from youtube_promoter.handler.taskHandler import TaskHandler


@click.command()
@click.argument('file', type=click.File('r'))
def run(file: click.File):
    config = json.loads(file.read())
    th = TaskHandler(config=config)
    for task in th.getTasks():
        task.process()
