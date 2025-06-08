from typing import List
from src.utils.logger import Logger
from src.service.interface_service import Service
from src.dao.interface_dao import Dao
from src.dao.article_dao import ArticleDao
from src.model import Article


logger = Logger(__name__)


class ArticleService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = ArticleDao()

    def add(
        self,
        subset_id: int,
        user_id: int,
        title: str,
        content: str,
        img_src: str,
        state: bool,
    ) -> bool:
        self._dao.add(subset_id, user_id, title, content, img_src, state)

    def update(self, *args, **kwargs) -> bool:
        pass

    def remove(self, article_id: int) -> bool:
        return self._dao.remove(article_id)

    def query_one(self, article_id: int) -> Article | None:
        return self._dao.query_one(article_id)

    def query_by_page(self, page: int, limit: int = 10) -> List[Article]:
        return self._dao.query_by_page(page, limit)

    def query_by_condition(
        self, state: bool, page: int, limit: int = 10
    ) -> List[Article]:
        return self._dao.query_by_condition(state, page, limit)

    def query_all(self) -> List[Article]:
        return self._dao.query_all()

    def count(self) -> int:
        return self._dao.count()

    def pages(self, page_size: int = 10) -> int:
        return self._dao.pages(page_size)
