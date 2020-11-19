import json
import click
import tornado.ioloop
import tornado.web
import xml.etree.ElementTree as XML
from youtube_promoter.services.pubsubhubhub import subscribe, handleUpdate
from youtube_promoter.handler.taskHandler import TaskHandler
from youtube_promoter.model.params import Params
from youtube_promoter.handler.resubscribe import Resubscribe

namespaces = {
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'xmlns': 'http://www.w3.org/2005/Atom'
}


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, config):
        self.config = config

    def link(self):
        resubscribe = Resubscribe(options=task["options"], params=self.params)
        resubscribe.process()

    def get(self):
        resp = subscribe(
            {
                "hub.mode":
                self.request.query_arguments['hub.mode'][0].decode(),
                "hub.challenge":
                self.request.query_arguments['hub.challenge'][0].decode(),
                "hub.verify_token":
                self.request.query_arguments['hub.verify_token'][0].decode()
            }, self.config)
        self.set_status(resp["statusCode"])
        self.write(resp["body"])

    def post(self):
        req = self.request.body.decode('utf-8')
        resp = handleUpdate(req, self.config)
        self.set_status(resp["statusCode"])
        self.write(resp["body"])


def make_app(config):
    return tornado.web.Application([
        (r"/youtube-callback", MainHandler, dict(config=config)),
    ])


@click.command()
@click.argument('file', type=click.File('r'))
def run(file: click.File):
    print("starting")
    config = json.loads(file.read())
    Params.testConfigValidity(config)
    print("starting :: server")
    app = make_app(config)
    server_port = config["server-port"]
    app.listen(server_port)
    print(f"INFO :: server running at port {server_port}")
    tornado.ioloop.IOLoop.current().start()
