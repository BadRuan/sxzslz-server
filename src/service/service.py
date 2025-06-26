from abc import ABCMeta
from abc import abstractmethod
from typing import List, TypeVar

T = TypeVar("T")


class Service(metaclass=ABCMeta):

    @abstractmethod
    def add(self, *args, **kwargs) -> bool: ...

    def remove(self, id: int) -> bool:
        if id <= 0:
            return False
        else:
            count: int = self.get_counts()
            if id > count:
                return False
        return self._dao.remove(id)

    def update(self, *args, **kwargs) -> bool: ...

    def query_one(self, id: int) -> T | None:
        if id <= 0:
            return None
        else:
            count: int = self.get_counts()
            if id > count:
                return None
        return self._dao.query_one(id)

    def query_by_page(self, page: int, limit: int) -> List[T]:
        if page <= 0 | limit <= 0:
            return []
        pages: int = self.get_pages(limit)
        if page > pages:
            page = pages
        return self._dao.query_by_condition(page, limit)

    def get_counts(self) -> int:
        return self._dao.get_counts()

    def get_pages(self, page_size: int) -> int:
        if page_size <= 0:
            return 1
        return self._dao.get_pages(page_size)
