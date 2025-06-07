from typing import List
from src.model import SubsetType
from src.service.interface_service import Service
from src.dao.interface_dao import Dao
from src.dao.subset_dao import SubsetDao
from src.model import SubsetType, Subset


class SubsetService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = SubsetDao()

    def add(
        self,
        subset_name: str,
        subset_type: SubsetType,
    ) -> bool:
        return self._dao.add(subset_name, subset_type)

    def remove(self, subset_id: int) -> bool:
        return self._dao.remove(subset_id)

    def update(self, subset_id: int, subset_name: str) -> bool:
        return self._dao.update(subset_id, subset_name)

    def query_one(self, subset_id: int) -> Subset | None:
        return self._dao.query_one(subset_id)

    def query_by_page(self, page: int, limit: int) -> List[Subset]:
        return self._dao.query_by_page(page, limit)

    def query_all(self) -> List[Subset]:
        return self._dao.query_all()

    def count(self) -> int:
        return self._dao.count()

    def pages(self, page_size: int = 10) -> int:
        return self._dao.pages(page_size)
