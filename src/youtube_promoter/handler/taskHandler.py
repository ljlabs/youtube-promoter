from youtube_promoter.handler.newVidTweet import NewVidTweet
from youtube_promoter.model.params import Params


class TaskHandler:
    def __init__(self, config):
        self.params = Params(config)
        self.tasks = config["tasks"]

    def getTasks(self):
        for task in self.tasks:
            if task["mode"] == "NEW-VID-TWEET":
                yield NewVidTweet(message_options=task["message-options"],
                                  params=self.params)
