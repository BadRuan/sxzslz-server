from abc import ABCMeta
from abc import abstractmethod
from typing import List, TypeVar

T = TypeVar("T")


class Dao(metaclass=ABCMeta):

    @abstractmethod
    def add(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def remove(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def update(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def query_one(self, *args, **kwargs) -> T | None: ...

    @abstractmethod
    def query_all(self) -> List[T]: ...

    @abstractmethod
    def count(self) -> int: ...
