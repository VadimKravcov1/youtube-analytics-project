
import os
from googleapiclient.discovery import build

os.environ.setdefault('API_KEY', 'AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
api_key = os.environ.get('API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)



class Video:


    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.title = video_response['items'][0]['snippet']['title']
            self.url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']
            self.quantity_all_views = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except:
            self.title = None
            self.url = None
            self.quantity_all_views = None
            self.like_count = None





    def __str__(self):
        return self.title



class PLVideo(Video):


    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        # self.video_id = video_id
        self.playlist_id = playlist_id












