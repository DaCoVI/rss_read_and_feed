from abc import ABC, abstractmethod
from typing import overload
import json
from typing import Any
from xml.parsers.expat import ExpatError

import xmltodict


class ContentParser(ABC):

    @abstractmethod
    def to_dict(self, content: str) -> dict[str, Any]: ...

    @overload
    def _normalize_none(self, data: dict[str, Any]) -> dict[str, Any]: ...

    @overload
    def _normalize_none(self, data: list[Any]) -> list[Any]: ...

    @overload
    def _normalize_none(self, data: None) -> str: ...

    def _normalize_none(
        self, data: dict[str, Any] | list[Any] | None
    ) -> dict[str, Any] | list[Any] | str:
        """
        Normalisiert rekursiv Werte in verschachtelten Datenstrukturen, indem
        `None` durch einen leeren String ersetzt wird.
        Das erleichtert nachfolgende Verarbeitungsschritte, die stringbasierte
        Felder erwarten.

        Args:
            data (dict[str, Any] | list[Any] | None):
                Die zu normalisierende Datenstruktur. Kann ein Dictionary,
                eine Liste oder `None` sein.

        Returns:
            dict[str, Any] | list[Any] | str:
                Die normalisierte Struktur. Dictionaries und Listen werden
                rekursiv bereinigt; `None` wird zu einem leeren String.
        """
        if isinstance(data, dict):
            return {k: self._normalize_none(v) for k, v in data.items()}
        elif data is None:
            return ""
        elif isinstance(data, list):
            return [self._normalize_none(v) for v in data]
        return data


class JsonContentParser(ContentParser):
    def to_dict(self, content: str) -> dict[str, Any]:
        try:
            data = json.loads(content)
            return self._normalize_none(data)
        except (TypeError, json.JSONDecodeError):
            return dict()


class XmlContentParser(ContentParser):
    def to_dict(self, content: str) -> dict[str, Any]:
        try:
            data = xmltodict.parse(content.strip())
            return self._normalize_none(data)
        except (AttributeError, ExpatError):
            return dict()
