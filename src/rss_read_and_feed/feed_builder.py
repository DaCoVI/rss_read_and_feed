from abc import ABC, abstractmethod
from datetime import datetime
from typing import Self
from rss_read_and_feed.dto.feed_item import FeedItem, YoutubeVideoItem


class FeedItemBuilder(ABC):
    @abstractmethod
    def reset(self) -> None: ...
    @abstractmethod
    def set_author(self, author: str) -> Self: ...
    @abstractmethod
    def set_title(self, title: str) -> Self: ...
    @abstractmethod
    def set_published(self, published: datetime) -> Self: ...
    @abstractmethod
    def set_link(self, link: str) -> Self: ...
    @abstractmethod
    def build(self) -> FeedItem: ...


class YoutubeVideoBuilder(FeedItemBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__dto = YoutubeVideoItem()

    def set_author(self, author: str) -> Self:
        self.__dto.author = author
        return self

    def set_title(self, title: str) -> Self:
        self.__dto.title = title
        return self

    def set_published(self, published: datetime) -> Self:
        self.__dto.published = published
        return self

    def set_link(self, link: str) -> Self:
        self.__dto.link = link
        if "/shorts/" in link:
            self.__dto.set_type_short()
        else:
            self.__dto.set_type_video()
        return self

    def set_updated(self, updated: datetime) -> Self:
        self.__dto.updated = updated
        return self

    def set_video_id(self, video_id: str) -> Self:
        self.__dto.video_id = video_id
        return self

    def set_channel_id(self, channel_id: str) -> Self:
        self.__dto.channel_id = channel_id
        return self

    def set_description(self, description: str) -> Self:
        self.__dto.description = description
        return self

    def build(self) -> YoutubeVideoItem:
        result = self.__dto
        self.reset()
        return result
