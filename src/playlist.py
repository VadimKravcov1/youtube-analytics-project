import datetime
import os
from googleapiclient.discovery import build
import isodate


os.environ.setdefault('API_KEY', 'AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
api_key = os.environ.get('API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)
class PlayList:


    def __init__(self,playlist_id):
        self.playlist_id = playlist_id

        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'

        playlists = youtube.playlists().list(channelId=channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        # printj(playlists)
        for playlist in playlists['items']:
            if playlist['id'] == self.playlist_id:
                # print(playlist)

                self.title = playlist['snippet']['title']


        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id


    @property
    def total_duration(self):
        playlist_id = self.playlist_id
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        # printj(video_response)
        total = datetime.timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total += duration
        return total


    def show_best_video(self):
        playlist_id = self.playlist_id
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        list1 = []

        for i in video_ids:
            video_id = i
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            list1.append(video_response)

        sll = sorted(list1, key=compare_by_likes)
        link = "https://youtu.be/" + sll[-1]['items'][0]['id']

        return link


def compare_by_likes(list):
    return int(list['items'][0]['statistics']['likeCount'])



























