from abc import ABCMeta
from abc import abstractmethod
from typing import List


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
    def query_one(self, *args, **kwargs):
        pass

    @abstractmethod
    def query_all(self) -> List:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
