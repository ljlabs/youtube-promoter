# Youtube Promoter

This is a basic tool which can be used for various youtube promotion tasks  
The hope is to build a large array of features which may be set using the  
*config.json* file alone.

## Requirements:
1. *Couch DB*
2. *Python 3*

## How to use:
The configuration of this application is simple and entirely handled by the  
*config.json* file.
### Auth
Please use the *config.json*, set all of the keys and youtube channel names.  
```JSON
{  
    "youtube-key": "",  
    "twitter-key": "",  
    "channel-name": ""  
}
```
### Tasks
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
### Task Modes
There are a set of mode's a task may complete:  
1. `NEW-VID-TWEET` A new video is uploaded to youtube and a tweet is posted  
to twitter

## What the future holds:
1. I hope to add liquid support to the message fields
2. Add models for the various fields of the *config.json* file with a validity checker