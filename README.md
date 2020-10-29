# Youtube Promoter

![Python tests](https://github.com/ljlabs/youtube-promoter/workflows/Python%20tests/badge.svg)

This is a basic tool which can be used for various youtube promotion tasks
The hope is to build a large array of features which may be set using the
*config.json* file alone.

This package can be hosted via the cli by means of a Tornado API, or may
be hosted with a third party cloud function provider such as AWS Lambda.

This project uses youtube push notifications to automatically promote your
newly created content.


## How to use:

### Installation

    python setup.py install

### Configuration

The configuration of this application is simple and entirely handled by the
*config.json* file.
#### Auth
Please use the *config.json*, set all of the keys and youtube channel names.
```JSON
{
    "youtube-api-key": "",
    "twitter-api-key": "",
    "twitter-api-secret": "",
    "twitter-api-access-token": "",
    "twitter-api-access-token-secret": "",
    "twitter-api-bearer": "",
    "channel-id": "",
    "server-port": 0,
    "pubsubhubhub_secret": "",
}
```
#### Tasks
The system runs a particular set of tasks which are defined as
```JSON
{
    "tasks": [
        {
            "mode": "",
            "message-options": [
                {
                    "title-contains": "",
                    "message": ""
                }
            ]
        }
    ]
}
```
#### Task Modes
There are a set of mode's a task may complete:
1. `NEW-VID-TWEET` A new video is uploaded to youtube and a tweet is posted
to twitter
    >A. `title-contains` is used to display different messages based on a particular title.
    Leave blank if not needed
    B. `message` is used to post to twitter please use the keywords listed below to get data from the video
    >    * *TITLE* will be replaced with the video title
    >    * *URL* will be replaced with the videos URL

## Contribution

### What the future holds:
1. I hope to add liquid support to the message fields
2. Add models for the various fields of the *config.json* file with a validity checker

### Development Installation

Create a virtual environment:

    pip install virtualenv
    python -m virtualenv env
    source ./env/bin/activate

Install supporting tools:

    sh .scripts/setup.sh

Install development version of `youtube-promoter`:

    python setup.py develop

### Running

    python -m youtube_promoter config.json

now you will need to expose the port which you configure using the *config.json* file.
I recommend using ngrok which can be found https://ngrok.com/
ngrok will give you a public domain name which will allow anybody to access your server
To connect your server to the youtube push notifications you will need to
follow the steps described at https://developers.google.com/youtube/v3/guides/push_notifications
**please not the pubsubhubhub_secret you set in the *config.json* will need to corrospond
to the *Verify token* used when subscribing to youtube push notifications**
ps this secret can be anything as long as they corrospond between these 2 locations

### Testing

All tests are written in with pytest. You can simply run the test suite with tox:

    $ tox
