from enum import Enum


class MediaType(tuple[str, ...], Enum):
    JSON = tuple(("application/json",))
    XML = tuple(
        (
            "application/xml",
            "text/xml",
            "application/rss+xml",
        )
    )
