from youtube_promoter.model.params import Params

base_model = {
    "youtube-api-key":
    "",
    "twitter-api-key":
    "",
    "twitter-api-secret":
    "",
    "twitter-api-access-token":
    "",
    "twitter-api-access-token-secret":
    "",
    "twitter-api-bearer":
    "",
    "channel-id":
    "",
    "couch-db-url":
    "",
    "couch-db-table":
    "",
    "tasks": [{
        "mode": "",
        "message-options": [{
            "title-contains": "",
            "message": ""
        }]
    }]
}


def test_invalid_model():
    try:
        params = Params(config=base_model)
    except:
        assert False
    assert True
