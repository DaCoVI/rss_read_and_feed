import datetime

from rss_read_and_feed.feed_builder import YoutubeVideoBuilder
from rss_read_and_feed.dto.feed_item import YoutubeVideoItem


def test_set_author():
    builder = YoutubeVideoBuilder()
    name = "Vivaldi"
    assert builder.set_author(name) is builder
    assert builder._YoutubeVideoBuilder__dto.author == "Vivaldi"  # pyright: ignore


def test_reset():
    builder = YoutubeVideoBuilder()
    name = "Vivaldi"
    builder.set_author(name)

    builder.reset()
    assert builder._YoutubeVideoBuilder__dto.author is None  # pyright: ignore


def test_set_title():
    builder = YoutubeVideoBuilder()
    name = "Leck mich im Arsch"
    assert builder.set_title(name) is builder
    assert (
        builder._YoutubeVideoBuilder__dto.title  # pyright: ignore
        == "Leck mich im Arsch"
    )


def test_set_published():
    builder = YoutubeVideoBuilder()
    date = datetime.datetime(
        year=1988, month=4, day=26, hour=14, minute=30, second=30, microsecond=500
    )
    assert builder.set_published(date) is builder
    assert builder._YoutubeVideoBuilder__dto.published == date  # pyright: ignore


def test_set_link():
    builder = YoutubeVideoBuilder()
    link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert builder.set_link(link) is builder
    assert (
        builder._YoutubeVideoBuilder__dto.link  # pyright: ignore
        == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )


def test_set_updated():
    builder = YoutubeVideoBuilder()
    date = datetime.datetime(
        year=1988, month=4, day=26, hour=14, minute=30, second=30, microsecond=500
    )
    assert builder.set_updated(date) is builder
    assert builder._YoutubeVideoBuilder__dto.updated == date  # pyright: ignore


def test_set_video_id():
    builder = YoutubeVideoBuilder()
    video_id = "dQw4w9WgXcQ"
    assert builder.set_video_id(video_id) is builder
    assert (
        builder._YoutubeVideoBuilder__dto.video_id == "dQw4w9WgXcQ"  # pyright: ignore
    )


def test_channel_id():
    builder = YoutubeVideoBuilder()
    channel_id = "UCuAXFkgsw1L7xaCfnd5JJOw"
    assert builder.set_channel_id(channel_id) is builder
    assert (
        builder._YoutubeVideoBuilder__dto.channel_id  # pyright: ignore
        == "UCuAXFkgsw1L7xaCfnd5JJOw"
    )


def test_set_description():
    builder = YoutubeVideoBuilder()
    description = "The official video for “Never Gonna Give You Up” by Rick Astley."
    assert builder.set_description(description) is builder
    assert (
        builder._YoutubeVideoBuilder__dto.description  # pyright: ignore
        == "The official video for “Never Gonna Give You Up” by Rick Astley."
    )


def test_build():
    builder = YoutubeVideoBuilder()
    builder.set_title("title")
    dto = builder.build()

    assert isinstance(dto, YoutubeVideoItem)
    assert builder._YoutubeVideoBuilder__dto.title is None  # pyright: ignore
