
import os
from googleapiclient.discovery import build

os.environ.setdefault('API_KEY', 'AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
api_key = os.environ.get('API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)



class Video:

    def __init__(self, video_id):
        self.video_id = video_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']
        self.quantity_all_views = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title


# video_id = 'gaoc9MPZ4bw'
# video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
#                                                id=video_id
#                                                ).execute()


class PLVideo:

    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        self.playlist_id = playlist_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']
        self.quantity_all_views = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title

'''
получить статистику видео по его id
получить id можно из адреса видео
https://www.youtube.com/watch?v=gaoc9MPZ4bw или https://youtu.be/gaoc9MPZ4bw
'''
# video_id = 'gaoc9MPZ4bw'
# video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
#                                        id=video_id
#                                        ).execute()
# printj(video_response)


# video_title: str = video_response['items'][0]['snippet']['title']
# view_count: int = video_response['items'][0]['statistics']['viewCount']
# like_count: int = video_response['items'][0]['statistics']['likeCount']
# comment_count: int = video_response['items'][0]['statistics']['commentCount']
#
#
# print(video_response)
#
# print(video_response['items'][0]['statistics']['likeCount'])











