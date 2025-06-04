from abc import ABCMeta
from abc import abstractmethod
from typing import List, TypeVar

T = TypeVar("T")


class Service(metaclass=ABCMeta):

    @abstractmethod
    def add(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def remove(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def update(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def query_one(self, *args, **kwargs) -> T | None:
        pass

    @abstractmethod
    def query_by_page(self, page: int, limit: int) -> List[T]: ...

    @abstractmethod
    def query_all(self) -> List[T]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def pages(self, page_size: int) -> int:
        pass
