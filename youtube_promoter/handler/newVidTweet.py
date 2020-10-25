from youtube_promoter.model.params import Params
from youtube_promoter.services.youtube import get_all_videos, get_channel_upload_id
from youtube_promoter.services.couchDB import CouchHandler
from youtube_promoter.services.twitter import TwitterHandler

def parse_message(template, video):
    new_message = ""
    for word in template.split(' '):
        if word == "TITLE":
            new_message += f"{video['snippet']['title']} "
        elif word == "URL":
            new_message += f"https://www.youtube.com/watch?v={video['snippet']['resourceId']['videoId']} "
        elif word == "\n":
            new_message += f"{word}"
        else:
            new_message += f"{word} "
    return new_message

class NewVidTweet:
    def __init__(self, message_options, params: Params):
        self.message_options = message_options
        self.params = params
        self.channel_upload_id = get_channel_upload_id(api_key=self.params.youtube_key, channel_id=self.params.channel_id)
        self.new_videos = []

    def get_tweets(self):
        for video in self.new_videos:
            for option in self.message_options:
                if option["title-contains"] in video['snippet']['title']:
                    yield parse_message(option['message'], video)


    def process(self):
        # check for new youtube videos
        all_videos = get_all_videos(api_key=self.params.youtube_key, channel_id=self.channel_upload_id)
        ch = CouchHandler(server_url=self.params.couch_db_url, db_name=self.params.couch_db_table)
        self.new_videos = ch.get_new_items(all_videos)

        # TODO: tell twitter about the new videos
        th = TwitterHandler(params=self.params)
        for tweet in self.get_tweets():
            th.post_tweet(tweet)


        # update db with new videos
        for new_video in self.new_videos:
            ch.upload(new_video)