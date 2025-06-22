from typing import List
from src.model import Subset, QueryCondition
from src.dao.dao import Dao
from src.dao.subset_dao import SubsetDao
from src.service.service import Service


class SubsetService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = SubsetDao()

    def add(
        self,
        subset_name: str,
    ) -> bool:
        return self._dao.add(subset_name)

    def remove(self, subset_id: int) -> bool:
        if subset_id <= 0:
            return False
        else:
            count: int = self.count()
            if subset_id > count:
                return False
        return self._dao.remove(subset_id)

    def update(self, subset_id: int, subset_name: str) -> bool:
        if subset_id <= 0:
            return False
        else:
            count: int = self.count()
            if subset_id > count:
                return False
        return self._dao.update(subset_id, subset_name)

    def query_one(self, subset_id: int) -> Subset | None:
        if subset_id <= 0:
            return None
        else:
            count: int = self.count()
            if subset_id > count:
                return None
        return self._dao.query_one(subset_id)

    def query_by_page(self, query_condition: QueryCondition) -> List[Subset]:
        return self._dao.query_by_condition(query_condition)

    def get_counts(self) -> int:
        return self._dao.get_counts()

    def get_pages(self, page_size: int = 10) -> int:
        if page_size <= 0:
            return 1
        return self._dao.get_pages(page_size)
