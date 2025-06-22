from typing import List
from src.utils.logger import Logger
from src.model import Article, QueryCondition
from src.dao.dao import Dao
from src.dao.article_dao import ArticleDao
from src.service.service import Service
from src.service.article_service import ArticleService


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

    def test_dao_query_by_page(self):
        dao: Dao = ArticleDao()
        query_condition: QueryCondition = QueryCondition(page=1, limit=10, onther=None)
        results: List[Article] = dao.query_by_condition(query_condition)
        assert len(results) > 0
        logger.debug(f"Dao层 Article对象  查询文章数据运行成功")

    def test_service_count_and_pages(self):
        service: Service = ArticleService()
        count: int = service.get_counts()
        pages: int = service.get_pages()
        logger.debug(f"Service层 Article对象 查询文章总数运行成功，共{count}个文章")

    def test_service_query_by_page(self):
        service: Service = ArticleService()
        pagination_condition: QueryCondition = QueryCondition(
            page=1, limit=20, onther=None
        )
        results: List[Article] = service.query_by_page(pagination_condition)
        assert len(results) > 0
        logger.debug(f"Service层 Article对象 批量查询文章数据运行成功")
