from abc import ABC, abstractmethod
from typing import Any, Type
from rss_read_and_feed.feed_converter import FeedConverter, YoutubeFeedConverter


class FeedConverterStrategy(ABC):
    @abstractmethod
    def _can_handle(self, data: dict[str, Any]) -> bool: ...

    @abstractmethod
    def create_converter(self) -> FeedConverter: ...


class FeedConverterFactory:
    _strategies: list[Type[FeedConverterStrategy]] = []

    @classmethod
    def register(cls):
        """Decorator der dafür sorgt, dass jede `FeedConverterStrategy`
        Strategie-Klasse, die ihn verwendet, automatisch in der
        internen Strategie-Liste der `FeedConverterFactory` registriert wird."""

        def decorator(strategy_class: Type[FeedConverterStrategy]):
            cls._strategies.append(strategy_class)
            return strategy_class

        return decorator

    @classmethod
    def create_converter(cls, data: dict[str, Any]) -> FeedConverter:
        """
        Wählt anhand der registrierten Strategien den passenden FeedConverter aus
        und initialisiert ihn mit den übergebenen Daten.

        Raises:
            ValueError: Wenn keine Strategie die Daten verarbeiten kann.
        """
        for strategy_class in cls._strategies:
            strategy = strategy_class()
            if strategy._can_handle(data):
                converter = strategy.create_converter()
                converter._set_data(data)
                return converter
        raise ValueError("No converter found for data structure")


@FeedConverterFactory.register()
class YoutubeFeedStrategy(FeedConverterStrategy):
    def _can_handle(self, data: dict[str, Any]) -> bool:
        """
        Prüft, ob diese Strategie die Struktur der übergebenen Daten
        verarbeiten kann.
        """
        if data is not None:
            feed: dict[str, Any] = data.get("feed", {})
            feed_namespace: str = feed.get("@xmlns:yt", "")
            return "youtube" in feed_namespace.lower()
        return False

    def create_converter(self) -> FeedConverter:
        return YoutubeFeedConverter()
