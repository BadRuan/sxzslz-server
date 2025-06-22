from typing import List
from src.utils.logger import Logger
from src.model import Subset, QueryCondition
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
        count: int = dao.get_counts()
        assert None == dao.query_one(count + 1)

    def test_service_count_and_pages(self):
        service: Service = SubsetService()
        count: int = service.get_counts()
        pages: int = service.get_pages()
        logger.debug(f"Service层 Subset对象 查询分类总数运行成功，共{count}个分类")

    def test_dao_query_by_page(self):
        dao: Dao = SubsetDao()
        query_condition: QueryCondition = QueryCondition(page=1, limit=10, onther=())
        results1: List[Subset] = dao.query_by_condition(query_condition)
        assert len(results1) > 0
        logger.debug(f"Dao层 Subset对象 批量查询分类数据运行成功")

    def test_service_query_by_page(self):
        service: Service = SubsetService()
        query_condition: QueryCondition = QueryCondition(page=1, limit=10, onther=())
        results1: List[Subset] = service.query_by_page(query_condition)
        assert len(results1) > 0
        logger.debug(f"Service层 Subset对象 批量查询分类数据运行成功")
