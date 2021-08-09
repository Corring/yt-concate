import urllib.request
import json
from yt_concate.settings import API_KEY

print(API_KEY)
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

def get_all_video_in_channel(channel_id):
    # v= 后头有的时候会接ID，通常是漫长一段字串。这里是基底
    base_video_url = 'https://www.youtube.com/watch?v='
    # API的网址，
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        # 链接网址
        inp = urllib.request.urlopen(url)
        # 回传结果
        resp = json.load(inp)

        # 做结果的解读
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)

        except KeyError:
            break

    return video_links


# 得到影片的所有网址
# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
