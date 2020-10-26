# Youtube Promoter

![Python tests](https://github.com/ljlabs/youtube-promoter/workflows/Python%20tests/badge.svg)

This is a basic tool which can be used for various youtube promotion tasks
The hope is to build a large array of features which may be set using the
*config.json* file alone.


## How to use:

### Installation

**A running instance of [CouchDB](https://docs.couchdb.org/en/stable/install/index.html) is required**

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
    "couch-db-url": "",
    "couch-db-table": "",
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


### Testing

All tests are written in with pytest. You can simply run the test suite with tox:

    $ tox
