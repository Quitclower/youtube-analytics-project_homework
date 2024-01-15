import json
import os
from googleapiclient.discovery import build
import isodate

from helper.youtube_api_manual import youtube, printj


class Channel:
    """Класс для ютуб-канала"""
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    printj(channel)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        api_key: str = os.getenv('API-KEY')
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(
            id=self.channel_id,
            part='snippet,statistics'
        ).execute()
        print(json.dumps(response, indent=2, ensure_ascii=False))

