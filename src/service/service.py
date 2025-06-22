from abc import ABCMeta
from abc import abstractmethod
from typing import List, TypeVar

T = TypeVar("T")


class Service(metaclass=ABCMeta):

    @abstractmethod
    def add(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def remove(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def update(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def query_one(self, *args, **kwargs) -> T | None: ...

    @abstractmethod
    def query_by_page(self, page: int, limit: int) -> List[T]: ...

    @abstractmethod
    def get_counts(self) -> int: ...

    @abstractmethod
    def get_pages(self, page_size: int) -> int: ...
