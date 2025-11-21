import pytest

from rss_read_and_feed.dto.enums.video_type import VideoType


def test_from_value_roundtrip() -> None:
    assert VideoType("SHORT") is VideoType.SHORT
    assert VideoType("VIDEO") is VideoType.VIDEO


def test_invalid_value_raises() -> None:
    with pytest.raises(ValueError):
        VideoType("REEL")
