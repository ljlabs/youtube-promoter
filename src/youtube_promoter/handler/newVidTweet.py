from youtube_promoter.model.params import Params
from youtube_promoter.services.youtube import get_all_videos, get_channel_upload_id
from youtube_promoter.services.twitter import TwitterHandler


def parse_message(template, video):
    new_message = ""
    for word in template.split(' '):
        if word == "TITLE":
            new_message += f"{video['title']} "
        elif word == "URL":
            new_message += f"https://www.youtube.com/watch?v={video['video_id']} "
        elif word == "\n":
            new_message += f"{word}"
        else:
            new_message += f"{word} "
    return new_message


class NewVidTweet:
    def __init__(self, options, params: Params, video):
        self.options = options
        self.params = params
        self.video = video
        self.channel_upload_id = get_channel_upload_id(
            api_key=self.params.youtube_key, channel_id=self.params.channel_id)
        self.new_videos = []

    def get_tweet(self):
        for option in self.options:
            if option["title-contains"] in self.video['title']:
                yield parse_message(option['message'], self.video)

    def process(self):
        th = TwitterHandler(params=self.params)
        for tweet in self.get_tweet():
            th.post_tweet(tweet)
