class Params:
    def __init__(self, config):
        self.youtube_key = config["youtube-api-key"]
        self.twitter_key = config["twitter-api-key"]
        self.twitter_secret = config["twitter-api-secret"]
        self.twitter_bearer = config["twitter-api-bearer"]
        self.twitter_api_access_token = config["twitter-api-access-token"]
        self.twitter_api_access_token_secret = config[
            "twitter-api-access-token-secret"]
        self.channel_id = config["channel-id"]
        self.couch_db_url = config["couch-db-url"]
        self.couch_db_table = config["couch-db-table"]
        self.check_state_validity()

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
        if self.couch_db_url == "":
            raise Exception("please set couch-db-url")
        if self.couch_db_table == "":
            raise Exception("please set couch-db-table")
