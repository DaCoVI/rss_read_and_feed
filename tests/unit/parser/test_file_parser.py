from typing import Any

from rss_read_and_feed.content_parser import ContentParser, JsonContentParser
from rss_read_and_feed.content_parser import XmlContentParser


class FileParserTest(ContentParser):
    def to_dict(self, content: str) -> Any:
        pass


def test_normalize_none():
    dummy = FileParserTest()
    assert dummy._normalize_none(None) == ""
    assert dummy._normalize_none({"key": None}) == {"key": ""}
    assert dummy._normalize_none({}) == {}
    assert dummy._normalize_none([None, "test"]) == ["", "test"]
    assert dummy._normalize_none({None: "test"}) == {None: "test"}  # pyright: ignore
    assert dummy._normalize_none("None") == "None"  # pyright: ignore
    assert dummy._normalize_none({"key": {"subkey": [None, None]}}) == {
        "key": {"subkey": ["", ""]}
    }


def test_convert_json_string():
    parser = JsonContentParser()
    contents: list[Any] = [
        None,
        1,
        "",
        '{"header": ""}',
        '{"header": {"a": "b", "n": "1"}}',
        '{"header": {"a": "true", "n": "1.1", "date": "2025-09-10 14:10:47.830585"}}',
    ]
    expecteds: list[dict[str, Any]] = [
        dict(),
        dict(),
        dict(),
        {"header": ""},
        {"header": {"a": "b", "n": "1"}},
        {"header": {"a": "true", "n": "1.1", "date": "2025-09-10 14:10:47.830585"}},
    ]
    for i in range(len(contents)):
        assert parser.to_dict(contents[i]) == expecteds[i]


def test_convert_xml_string():
    parser = XmlContentParser()
    contents: list[Any] = [
        None,
        1,
        "",
        "<header></header>",
        "<header><a>b</a><n>1</n></header>",
        "<header><a>true</a><n>1.1</n><date>2025-09-10 14:10:47.830585</date></header>",
    ]
    expecteds: list[dict[str, Any]] = [
        dict(),
        dict(),
        dict(),
        {"header": ""},
        {"header": {"a": "b", "n": "1"}},
        {"header": {"a": "true", "n": "1.1", "date": "2025-09-10 14:10:47.830585"}},
    ]
    for i in range(len(contents)):
        assert parser.to_dict(contents[i]) == expecteds[i]
