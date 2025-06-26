from typing import List
from src.utils.logger import Logger
from src.model import Subset
from src.dao.dao import Dao
from src.dao.subset_dao import SubsetDao
from src.service.service import Service
from src.service.subset_service import SubsetService


logger = Logger(__name__)


class TestSubset:

    # def test_insert_subset(self):
    #     dao: Dao = SubsetDao()
    #     dao.add("泵站新闻")
    #     dao.add("通知公告")
    #     dao.add("文件公示")
    #     dao.add("招投标采购")
    #     logger.info("分类插入成功")

    def test_dao_query_one(self):
        dao: Dao = SubsetDao()
        assert None != dao.query_one(1)

    def test_dao_query_by_page(self):
        dao: Dao = SubsetDao()
        page, limit = 1, 10
        results1: List[Subset] = dao.query_by_condition(page, limit)
        assert len(results1) > 0

    def test_service_query_by_page(self):
        service: Service = SubsetService()
        page, limit = 1, 10
        results1: List[Subset] = service.query_by_page(page, limit)
        assert len(results1) > 0
