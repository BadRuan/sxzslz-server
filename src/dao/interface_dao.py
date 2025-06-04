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
        sql: str = (
            f"DELETE FROM `{self.table_name}` WHERE {self.primary_key_name} = '{primary_key_id}'"
        )
        with Storage() as storage:
            storage.remove(sql)
            return True
        return False

    def count(self) -> int:
        sql: str = f"SELECT COUNT(*) AS 'count' FROM `{self.table_name}`"
        with Storage() as storage:
            result = storage.query_one(sql)
            return result["count"]
