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
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_id = self.channel_id 
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)
