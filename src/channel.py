import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

#import isodate

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
# api_key = os.environ['YT_API_KEY']
# print(api_key)
# for key in os.environ:
#     print(key, '--', os.environ[key])
os.environ.setdefault('API_KEY', 'AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')
api_key = os.environ.get('API_KEY')
# print(os.environ.get('API_KEY'))
# создать специальный объект для работы с API

youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.channel_descr = channel['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/" + channel['items'][0]['snippet']['customUrl']
        self.quantity_sub = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.quantity_all_views = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)

    def to_json(self, file_name):
        with open(file_name, 'wt') as file:
            text = {'channel_id':self.__channel_id, 'title':self.title,
                    'channel_descr':self.channel_descr, 'url':self.url,
                    'quantity_sub':self.quantity_sub, 'video_count':self.video_count,
                    'quantity_all_views':self.quantity_all_views}
            json_text = json.dumps(text, ensure_ascii=False, indent=2)
            file.write(json_text)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey='AIzaSyDp1Tf3pPXCN2lJ2Mzs-k7Zwr8v-pg4vrI')

    @property
    def channel_id(self):
        return self.__channel_id


    # channel_id = self.channel_id
    # channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    # print(channel)



#channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# print(channel)
# channel_name = channel['items'][0]['snippet']['title']
# print(channel_name)
# channel_descr = channel['items'][0]['snippet']['description']
# print(channel_descr)
# channel_link = "https://www.youtube.com/" + channel['items'][0]['snippet']['customUrl']
# print(channel_link)
# quantity_sub = channel['items'][0]['statistics']['subscriberCount']
# print(quantity_sub)
# quantity_vid = channel['items'][0]['statistics']['videoCount']
# print(quantity_vid)
# quantity_all_views = channel['items'][0]['statistics']['viewCount']
# print(quantity_all_views)











