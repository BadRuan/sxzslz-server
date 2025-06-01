from abc import ABCMeta
from abc import abstractmethod
from typing import List


class Dao(metaclass=ABCMeta):

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
    def query_one(self, *args, **kwargs):
        pass

    @abstractmethod
    def query_all(self, *args, **kwargs) -> List:
        pass

    @abstractmethod
    def count(self, *args, **kwargs) -> int:
        pass
