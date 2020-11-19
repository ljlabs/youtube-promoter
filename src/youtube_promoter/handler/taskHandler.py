from youtube_promoter.handler.newVidTweet import NewVidTweet
from youtube_promoter.handler.resubscribe import Resubscribe
from youtube_promoter.model.params import Params


class TaskHandler:
    def __init__(self, config, video):
        self.params = Params(config)
        self.video = video
        self.tasks = config["tasks"]

    def getTasks(self):
        for task in self.tasks:
            if task["mode"] == "NEW-VID-TWEET":
                yield NewVidTweet(options=task["options"],
                                  params=self.params,
                                  video=self.video)
            if task["mode"] == "RESUBSCRIBE":
                yield Resubscribe(options=task["options"], params=self.params)
