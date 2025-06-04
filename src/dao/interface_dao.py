from abc import ABCMeta
from abc import abstractmethod
from typing import List, TypeVar
from src.utils.storage import Storage


T = TypeVar("T")


class Dao(metaclass=ABCMeta):

    def __init__(self, table_name: str, primary_key_name: str):
        self.table_name: str = table_name
        self.primary_key_name: str = primary_key_name

    @abstractmethod
    def add(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def update(self, *args, **kwargs) -> bool: ...

    @abstractmethod
    def query_one(self, *args, **kwargs) -> T | None: ...

    @abstractmethod
    def query_by_page(self, page: int, limit: int) -> List[T]: ...

    @abstractmethod
    def query_all(self) -> List[T]: ...

    def remove(self, primary_key_id: int) -> bool:
        sql: str = "DELETE FROM `%s` WHERE %s = '%s'" % (
            self.table_name,
            self.primary_key_name,
            primary_key_id,
        )

        with Storage() as storage:
            storage.remove(sql)
            return True
        return False

    def count(self) -> int:
        sql: str = "SELECT COUNT(*) AS 'count' FROM `%s`" % self.table_name
        with Storage() as storage:
            result = storage.query_one(sql)
            return result["count"]

    def pages(self, page_size: int) -> int:
        sql: str = "SELECT COUNT(*) as 'count' FROM `%s`" % self.table_name
        with Storage() as storage:
            total_records = storage.query_one(sql)
            total_pages: int = (total_records["count"] + page_size - 1) // page_size
            return total_pages
        return 0
