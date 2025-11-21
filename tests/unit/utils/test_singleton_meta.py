# mypy: disable-error-code=no-untyped-def

import threading
import time
from typing import Generator

import pytest
from rss_read_and_feed.utils.singleton_meta import Singleton


@pytest.fixture(autouse=True)
def isolate_singleton_registry(
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[None, None, None]:
    monkeypatch.setattr(Singleton, "_instances", {}, raising=False)
    Service.init_calls = 0
    yield


class Service(metaclass=Singleton):
    init_calls = 0

    def __init__(self, x: int = 0) -> None:
        time.sleep(0.01)
        type(self).init_calls += 1
        self.x = x


def test_returns_same_instance():
    a = Service(1)
    b = Service(2)
    assert a is b
    assert Service.init_calls == 1
    assert a.x == 1


def test_seperate_singletons_per_class():
    class Other(metaclass=Singleton):
        pass

    s = Service()
    o = Other()

    assert s is Service()
    assert o is Other()
    assert o is not s


def test_thread_safety_single_init():
    results: list[Service] = []

    def worker():
        results.append(Service(42))

    threads = [threading.Thread(target=worker) for _ in range(50)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert len({id(x) for x in results}) == 1
    assert Service.init_calls == 1
    assert results[0].x == 42
