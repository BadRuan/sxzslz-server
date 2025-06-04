from src.utils.logger import Logger
from src.dao.interface_dao import Dao
from src.dao.article_dao import ArticleDao


logger = Logger(__name__)


class TestArticle:

    # def test_add_article(self):
    #     dao: Dao = ArticleDao()
    #     dao.add(
    #         user_id=1,
    #         title="测试文件发布5",
    #         content="测试内容333",
    #         img_src="http://badruan.onlin1e",
    #         state=False,
    #     )
    #     dao.add(
    #         user_id=1,
    #         title="测试文件发布6",
    #         content="测试内容4444",
    #         img_src="http://badruan.onlin1e",
    #         state=True,
    #     )
    def test_query_all(self):
        dao: Dao = ArticleDao()
        for i in dao.query_all():
            logger.debug(f"Article: {i}")

    def test_all_query_all(self):
        dao: Dao = ArticleDao()
        assert len(dao.query_all()) == dao.count()
