from typing import List
from src.utils.logger import Logger
from src.model import Article
from src.dao.dao import Dao
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

    def test_dao_query_by_page(self):
        dao: Dao = ArticleDao()
        subset, page, limit = 1, 1, 10
        results: List[Article] = dao.query_by_condition(subset, page, limit)
        assert len(results) > 0
        logger.debug(f"Dao层 Article对象  查询文章数据运行成功")

    # def test_service_query_by_page(self):
    #     service: Service = ArticleService()
    #     pagination_condition: QueryCondition = QueryCondition(
    #         page=1, limit=20, onther=(1,)
    #     )
    #     results: List[Article] = service.query_by_page(pagination_condition)
    #     assert len(results) > 0
    #     logger.debug(f"Service层 Article对象 批量查询文章数据运行成功")

    def test_dao_update(self):
        dao: Dao = ArticleDao()
        result = dao.update(
            2,
            "沈巷镇水利站文章",
            '<h2>Hello 沈巷镇水利站</h2><p><br></p><p>这是文章书写<u>测试</u>，主要<span style="color: rgb(231, 95, 51);"><strong>关心</strong></span>后面是否能按<em>预期</em>样式显示内容。</p><p><br></p><ol><li>计划任务1</li><li>计划任务2</li></ol>',
        )
        assert result

    def test_add_read_count(self):
        dao: Dao = ArticleDao()
        result: bool = dao.add_read_count(1)
        assert result

    def test_dao_query_one(self):
        dao: Dao = ArticleDao()
        article: Article = dao.query_one(0)
        assert None == article
