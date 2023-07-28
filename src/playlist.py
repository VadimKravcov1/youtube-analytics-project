from src.channel import Channel
import datetime
import isodate
class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        youtube_obj = Channel.get_service()

        playlists = youtube_obj.playlists().list(id=playlist_id,
                                                 part='contentDetails,snippet',
                                                 maxResults=50,
                                                 ).execute()

        playlist_videos = youtube_obj.playlistItems().list(playlistId=playlist_id,
                                                           part='contentDetails',
                                                           maxResults=50,
                                                           ).execute()

        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        self.title = playlists['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        youtube_obj = Channel.get_service()
        playlist_id = self.playlist_id
        playlist_videos = youtube_obj.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube_obj.videos().list(part='contentDetails,statistics',
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
        youtube_obj = Channel.get_service()
        playlist_id = self.playlist_id
        playlist_videos = youtube_obj.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        list1 = []

        for i in video_ids:
            video_id = i
            video_response = youtube_obj.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            list1.append(video_response)

        sll = sorted(list1, key=compare_by_likes)
        link = "https://youtu.be/" + sll[-1]['items'][0]['id']

        return link


def compare_by_likes(list):
    return int(list['items'][0]['statistics']['likeCount'])