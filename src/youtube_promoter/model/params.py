class Params:
    def __init__(self, config):
        self.youtube_key = config.get("youtube-api-key", "")
        self.twitter_key = config.get("twitter-api-key", "")
        self.twitter_secret = config.get("twitter-api-secret", "")
        self.twitter_bearer = config.get("twitter-api-bearer", "")
        self.twitter_api_access_token = config.get("twitter-api-access-token",
                                                   "")
        self.twitter_api_access_token_secret = config.get(
            "twitter-api-access-token-secret", "")
        self.channel_id = config.get("channel-id", "")
        self.server_port = config.get("server-port", 0)
        self.pubsubhubhub_secret = config.get("pubsubhubhub-secret", "")
        self.check_state_validity()

    @classmethod
    def testConfigValidity(cls, config):
        Params(config)

    def check_state_validity(self):
        if self.youtube_key == "":
            raise Exception("please set youtube-api-key")
        if self.twitter_key == "":
            raise Exception("please set twitter-api-key")
        if self.twitter_secret == "":
            raise Exception("please set twitter-api-secret")
        if self.twitter_api_access_token == "":
            raise Exception("please set twitter-api-access-token")
        if self.twitter_api_access_token_secret == "":
            raise Exception("please set twitter-api-access-token-secret")
        if self.twitter_bearer == "":
            raise Exception("please set twitter-api-bearer")
        if self.channel_id == "":
            raise Exception("please set channel-id")
        if self.server_port == "":
            raise Exception("please set server-port")
        if self.pubsubhubhub_secret == "":
            raise Exception("please set pubsubhubhub-secret")
