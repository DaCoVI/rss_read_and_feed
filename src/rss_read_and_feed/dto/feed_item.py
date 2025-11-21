from abc import ABC
from datetime import datetime
from typing import Any, override

from rss_read_and_feed.dto.enums.video_type import VideoType


class FeedItem(ABC):
    def __init__(self) -> None:
        self.__author: str | None = None
        self.__title: str | None = None
        self.__published: datetime | None = None
        self.__link: str | None = None

    @property
    def author(self) -> str | None:
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        self.__author = value

    @property
    def title(self) -> str | None:
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    @property
    def published(self) -> datetime | None:
        return self.__published

    @published.setter
    def published(self, value: datetime | None) -> None:
        self.__published = value

    @property
    def link(self) -> str | None:
        return self.__link

    @link.setter
    def link(self, value: str | None) -> None:
        self.__link = value

    def to_dict(self) -> dict[str, Any]:
        dictionary: dict[str, Any] = {}
        for attr, value in self.__dict__.items():
            if attr.startswith("__"):
                attr = attr.split("__")[-1]
            elif attr.startswith("_"):
                attr = attr[1:]
            dictionary[attr] = value
        return dictionary

    def __str__(self) -> str:
        return f"'{self.author}' published '{self.title}'\n"


class YoutubeVideoItem(FeedItem):
    def __init__(self) -> None:
        super().__init__()
        self.__updated: datetime | None = None
        self.__video_id: str | None = None
        self.__channel_id: str | None = None
        self.__description: str | None = None
        self.__type: VideoType | None = None

    def set_type_short(self) -> None:
        self.__type = VideoType.SHORT

    def set_type_video(self) -> None:
        self.__type = VideoType.VIDEO

    @property
    def channel_id(self) -> str | None:
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value: str | None) -> None:
        self.__channel_id = value

    @property
    def description(self) -> str | None:
        return self.__description

    @description.setter
    def description(self, value: str | None) -> None:
        self.__description = value

    @property
    def video_id(self) -> str | None:
        return self.__video_id

    @video_id.setter
    def video_id(self, value: str | None) -> None:
        self.__video_id = value

    @property
    def updated(self) -> datetime | None:
        return self.__updated

    @updated.setter
    def updated(self, value: datetime | None) -> None:
        self.__updated = value

    @property
    def type(self) -> None | VideoType:
        return self.__type

    @override
    def __str__(self) -> str:
        return (
            f"'{self.author}' published "
            f"{'' if self.type is None else 'a ' + self.type.value.lower() + ": "}"
            f"'{self.title}'\n"
        )
