import datetime
import os
from googleapiclient.discovery import build
import isodate


# os.environ.setdefault('API_KEY', 'AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
# api_key = os.environ.get('API_KEY')
#
#youtube = build('youtube', 'v3', developerKey=api_key)

class MixinLog:

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey='AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')

        return youtube

class PlayList(MixinLog):

    MixinLog.get_service()

    def __init__(self,playlist_id):
        # self.playlist_id = playlist_id

        self.__playlist_id = playlist_id

        playlist_info = self.get_service().playlists().list(id=self.__playlist_id,

                                                            part='snippet',

                                                            ).execute()

        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'

        playlists = youtube.playlists().list(channelId=channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        # printj(playlists)
        for playlist in playlists['items']:
            if playlist['id'] == self.__playlist_id:
                # print(playlist)

                self.title = playlist['snippet']['title']


        self.url = 'https://www.youtube.com/playlist?list=' + self.__playlist_id


    @property
    def total_duration(self):
        playlist_id = self.__playlist_id
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
        playlist_id = self.__playlist_id
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


#---------------------------------------



from src.channel import Channel
import datetime
import isodate


class PlayList:

    def __init__(self, playlist_id):
        youtube_obj = Channel.get_service()
        youtube = build('youtube', 'v3', developerKey='AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
        playlists = youtube_obj.playlists().list(id=playlist_id,
                                                 part='contentDetails,snippet',
                                                 maxResults=50,
                                                 ).execute()

        playlist_videos = youtube_obj.playlistItems().list(playlistId=playlist_id,
                                                           part='contentDetails',
                                                           maxResults=50,
                                                           ).execute()

        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        self.video_response = youtube_obj.videos().list(part='contentDetails,statistics',
                                                        id=','.join(video_ids)
                                                        ).execute()['items']

        self.title = playlists['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @property
    def total_duration(self):
        videos = [item['contentDetails']['duration'] for item in self.video_response]
        time = sum([isodate.parse_duration(i).seconds for i in videos])
        return datetime.timedelta(seconds=time)



    def show_best_video(self):
        max_likes = max([int(item['statistics']['likeCount']) for item in self.video_response])
        max_likes_video = [video['id'] for video in self.video_response if
                           video['statistics']['likeCount'] == str(max_likes)][0]
        return f"https://youtu.be/{max_likes_video}"




















