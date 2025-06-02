from typing import List
from src.model import SubsetType
from src.service.interface_service import Service
from src.dao.interface_dao import Dao
from src.dao.subset_dao import SubsetDao


class SubsetService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = SubsetDao()

    def add(
        self,
        subset_name: str,
        subset_type: SubsetType,
    ) -> bool:
        self._dao.add(subset_name, subset_type)

    def remove(self, subset_id: int) -> bool:
        self._dao.remove(subset_id)

    def update(self, subset_id: int, subset_name: str) -> bool:
        self._dao.update(subset_id, subset_name)

    def query_one(self, subset_id: int):
        self._dao.query_one(subset_id)

    def query_all(self) -> List:
        self._dao.query_all()

    def count(self) -> int:
        self._dao.count()
