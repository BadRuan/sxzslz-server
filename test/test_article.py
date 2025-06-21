from typing import List
from src.utils.logger import Logger
from src.model import Article, QueryCondition
from src.dao.interface_dao import Dao
from src.dao.article_dao import ArticleDao


logger = Logger(__name__)


class TestArticle:

    # def test_add_article(self):
    #     dao: Dao = ArticleDao()
    #     for i in range(1, 20):
    #         dao.add(
    #             subset_id=1,
    #             user_id=1,
    #             title=f"测试文件发布{i}",
    #             content="3测试内容测试内容测试内容测试内容33",
    #             img_src="http://badruan.onlin1e",
    #             state=False,
    #         )
    #     for i in range(10, 40):
    #         dao.add(
    #             subset_id=2,
    #             user_id=1,
    #             title=f"测试文件草稿{i}",
    #             content="测试内容测试内容测试内容测试内容测试内容测试内容",
    #             img_src="http://badruan.onlin1e",
    #             state=True,
    #         )

    def test_query_by_conditon(self):
        dao: Dao = ArticleDao()
        query_condition: QueryCondition = QueryCondition(page=1, limit=10, onther=None)
        results1: List[Article] = dao.query_by_condition(query_condition)
        assert len(results1) > 0
