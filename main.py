import requests


from rss_read_and_feed.feed_strategy import FeedConverterFactory
from rss_read_and_feed.parser_factory import ContentParserFactory


class HTTP:
    @staticmethod
    def get_response(
        url: str,
    ) -> tuple[requests.models.CaseInsensitiveDict[str], str]:
        response = requests.get(url)
        if not response.status_code == 200:
            raise requests.HTTPError(f"Could not get response from {url=}")
        return response.headers, response.text


def main() -> None:
    url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC9x0AN7BWHpCDHSm9NiJFJQ"
    header, content = HTTP.get_response(url)
    content_as_dict = ContentParserFactory.create_parser(header).to_dict(content)
    feed_list = FeedConverterFactory.create_converter(content_as_dict).to_dto_list()
    for feed in feed_list:
        print(feed)


if __name__ == "__main__":
    main()
