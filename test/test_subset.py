from typing import List
from src.utils.logger import Logger
from src.model import Subset, QueryCondition
from src.dao.interface_dao import Dao
from src.dao.subset_dao import SubsetDao


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
        count: int = dao.count()
        assert None == dao.query_one(count + 1)

    def test_dao_query_by_page(self):
        dao: Dao = SubsetDao()
        query_condition: QueryCondition = QueryCondition(page=1, limit=10, onther=())
        results1: List[Subset] = dao.query_by_condition(query_condition)
        assert len(results1) > 0
