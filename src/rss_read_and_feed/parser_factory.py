from abc import ABC, abstractmethod
from typing import Any, Callable, Type
from rss_read_and_feed.content_parser import (
    ContentParser,
    JsonContentParser,
    XmlContentParser,
)
from rss_read_and_feed.enums.parser import MediaType
from requests.models import CaseInsensitiveDict


class ParserProvider(ABC):
    @abstractmethod
    def get_parser(self) -> ContentParser: ...


class ContentParserFactory:
    __factories: dict[Type[ParserProvider], tuple[str, ...]] = {}

    @classmethod
    def register(
        cls, media_types: tuple[str, ...]
    ) -> Callable[[Type[ParserProvider]], Type[ParserProvider]]:
        """Decorator zum Registrieren eines ParserProviders für bestimmte MIME-Types.

        Beim Dekorieren einer Klasse, die von `ParserProvider` erbt, wird diese
        Klasse zusammen mit den angegebenen MIME-Types in der internen
        Factory-Registrierung (`__factories`) hinterlegt. Dadurch kann die
        Factory später anhand des 'Content-Type' eines HTTP-Responses automatisch
        den passenden ParserProvider auswählen.

        Args:
            media_types (tuple[str, ...]):
                Ein oder mehrere MIME-Types, die dem ParserProvider zugeordnet
                werden sollen (z.B. ("application/json",)).

        Returns:
            Callable:
                Ein Decorator, der die übergebene Provider-Klasse registriert und
                unverändert zurückgibt.
        """

        def decorator(factory_class: Type[ParserProvider]) -> Type[ParserProvider]:
            cls.__factories[factory_class] = media_types
            return factory_class

        return decorator

    @classmethod
    def create_parser(cls, headers: CaseInsensitiveDict[Any]) -> ContentParser:
        """Erzeugt einen passenden ContentParser basierend auf dem 'Content-Type'
        des übergebenen Response-Headers.

        Die Methode durchsucht alle zuvor registrierten ParserProvider und prüft,
        ob deren zugeordnete MIME-Types mit dem Content-Type des Headers
        übereinstimmen. Wird ein kompatibler ParserProvider gefunden, liefert die
        Methode dessen Parser-Instanz zurück.

        Args:
            headers (CaseInsensitiveDict[Any]):
                Header-Objekt eines HTTP-Response, aus dem der 'Content-Type'
                ausgelesen wird.

        Raises:
            ValueError: Wenn der Content-Type kein String ist oder kein passender
            ParserProvider für den angegebenen MIME-Type gefunden wurde.

        Returns:
            ContentParser: Eine Instanz des passenden Parsers.
        """
        content_type = headers.get("Content-Type", "")
        if not isinstance(content_type, str):
            raise ValueError(f"{type(content_type)=}")
        for factory_class, media_types in cls.__factories.items():
            if any(content_type.startswith(mt) for mt in media_types):
                return factory_class().get_parser()
        raise ValueError("No parser found")


@ContentParserFactory.register(MediaType.JSON)
class JsonParserProvider(ParserProvider):
    def get_parser(self) -> ContentParser:
        return JsonContentParser()


@ContentParserFactory.register(MediaType.XML)
class XmlParserProvider(ParserProvider):
    def get_parser(self) -> ContentParser:
        return XmlContentParser()
