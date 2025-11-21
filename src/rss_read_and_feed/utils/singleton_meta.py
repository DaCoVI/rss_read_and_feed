from abc import ABCMeta
from threading import Lock
from typing import Any, Type, TypeVar, cast


T = TypeVar("T")


class Singleton(type):
    _instances: dict[Type[Any], Any] = {}
    _lock: Lock = Lock()

    def __call__(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        with Singleton._lock:
            if cls not in Singleton._instances:
                instance = type.__call__(cls, *args, **kwargs)
                Singleton._instances[cls] = instance
        return cast(T, Singleton._instances[cls])


class SingletonABCMeta(Singleton, ABCMeta):
    pass
