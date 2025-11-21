from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from rss_read_and_feed.dto.feed_item import FeedItem
from rss_read_and_feed.feed_builder import YoutubeVideoBuilder


class FeedConverter(ABC):
    @abstractmethod
    def _set_data(self, data: dict[str, Any]) -> None: ...

    @abstractmethod
    def to_dto_list(self) -> list[FeedItem]: ...


class YoutubeFeedConverter(FeedConverter):
    def __init__(self, builder: YoutubeVideoBuilder | None = None) -> None:
        self.__builder: YoutubeVideoBuilder = (
            YoutubeVideoBuilder() if builder is None else builder
        )

    def _set_data(self, data: dict[str, Any]) -> None:
        self.__data = data

    def to_dto_list(self) -> list[FeedItem]:
        dto_list: list[FeedItem] = []
        for entry in self.data["feed"]["entry"]:
            dto = (
                self.__builder.set_author(entry["author"]["name"])
                .set_title(entry["title"])
                .set_published(datetime.fromisoformat(entry["published"]))
                .set_updated(datetime.fromisoformat(entry["updated"]))
                .set_link(entry["link"]["@href"])
                .set_video_id(entry["yt:videoId"])
                .set_channel_id(entry["yt:channelId"])
                .set_description(entry["media:group"]["media:description"])
                .build()
            )
            dto_list.append(dto)
        return dto_list

    @property
    def data(self) -> dict[str, Any]:
        return self.__data
