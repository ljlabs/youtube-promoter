from twython import Twython
from youtube_promoter.model.params import Params


class TwitterHandler:
    def __init__(self, params: Params):
        self.client = Twython(
            params.twitter_key, 
            params.twitter_secret,
            params.twitter_api_access_token, 
            params.twitter_api_access_token_secret
        )
    
    def post_tweet(self, status):
        self.client.update_status(status=status)
