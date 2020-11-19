# from youtube_promoter.model.params import Params
import requests


class Resubscribe:
    def __init__(self, options, params):  #: Params):
        self.options = options
        self.params = params

    def process(self):
        url = "https://pubsubhubbub.appspot.com/subscribe"

        payload=f"hub.callback={self.options['callback']}&" + \
        f"hub.topic={self.options['topic']}&" + \
        "hub.verify=sync&" + \
        "hub.mode=subscribe&" + \
        f"hub.verify_token={self.options['verify_token']}&" + \
        f"hub.secret={self.options['secret']}&" + \
        f"hub.lease_seconds={self.options['lease_seconds']}"
        headers = {
            'User-Agent':
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://pubsubhubbub.appspot.com',
            'Connection': 'keep-alive',
            'Referer': 'https://pubsubhubbub.appspot.com/subscribe',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


if __name__ == "__main__":
    resub = Resubscribe(options={
        "callback":
        "https://tys2d1kiwc.execute-api.us-east-2.amazonaws.com/prod/youtube-callback",
        "topic":
        "https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCyi-1SDaJxVG3SG9N1VvRsA",
        "verify_token": "some_url_safe_secret",
        "secret": "",
        "lease_seconds": 31536000
    },
                        params={})
    resub.process()
