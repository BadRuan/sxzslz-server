from typing import List
from src.utils.logger import Logger
from src.model import Subset, SubsetType
from src.dao.interface_dao import Dao
from src.dao.subset_dao import SubsetDao
from src.service.interface_service import Service
from src.service.subset_service import SubsetService


logger = Logger(__name__)


class TestSubset:

    def test_query_all(self):
        dao: Dao = SubsetDao()
        service: Service = SubsetService()
        assert len(dao.query_all()) == dao.count()
        assert len(service.query_all()) == service.count()

    def test_dao_query_one(self):
        dao: Dao = SubsetDao()
        count: int = dao.count()
        assert None == dao.query_one(count + 1)

    def test_dao_query_by_page(self):
        dao: Dao = SubsetDao()
        page, limit = 1, 10
        results: List[Subset] = dao.query_by_page(page, limit)
        assert len(results) > 0

    def test_dao_query_subset_by_type(self):
        dao: Dao = SubsetDao()
        service: Service = SubsetService()
        page, limit = 1, 10
        results1: List[Subset] = dao.query_by_condition(SubsetType.Article, page, limit)
        results2: List[Subset] = service.query_by_condition(
            SubsetType.Article, page, limit
        )
        assert len(results1) > 0
        assert len(results2) > 0
