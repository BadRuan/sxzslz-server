from typing import List
from src.utils.logger import Logger
from src.model import Article
from src.dao.interface_dao import Dao
from src.dao.article_dao import ArticleDao
from src.service.interface_service import Service
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
    #     for i in range(1, 10):
    #         dao.add(
    #             subset_id=1,
    #             user_id=1,
    #             title=f"测试文件草稿{i}",
    #             content="测试内容测试内容测试内容测试内容测试内容测试内容",
    #             img_src="http://badruan.onlin1e",
    #             state=True,
    #         )

    def test_query_all(self):
        dao: Dao = ArticleDao()
        service: Service = ArticleService()
        assert len(dao.query_all()) == dao.count()
        assert len(service.query_all()) == service.count()

    def test_query_by_page(self):
        dao: Dao = ArticleDao()
        page, limit = 2, 10
        results: List[Article] = dao.query_by_page(page, limit)
        assert len(results) > 0

    def test_query_by_conditon(self):
        dao: Dao = ArticleDao()
        service: Service = ArticleService()
        page, limit = 2, 10
        results1: List[Article] = dao.query_by_condition(True, page, limit)
        results2: List[Article] = service.query_by_condition(True, page, limit)
        assert len(results1) > 0
        assert len(results2) > 0
