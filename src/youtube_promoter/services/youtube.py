import requests
from youtube_promoter.model.params import Params


def get_channel_upload_id(api_key: str, channel_id: str) -> str:
    url = f"https://www.googleapis.com/youtube/v3/channels?id={channel_id}&key={api_key}&part=contentDetails"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json(
    )['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def get_all_videos(api_key: str, channel_id: str):
    items = []
    pageToken = ""
    while pageToken is not None:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?playlistId={channel_id}&key={api_key}&part=snippet&maxResults=50"
        if pageToken != "":
            url += f"&pageToken={pageToken}"
        response = requests.request("GET", url, headers={}, data={}).json()
        items += response['items']
        pageToken = response.get('nextPageToken', None)

    return items
