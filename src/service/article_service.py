from typing import List
from src.utils.logger import Logger
from src.model import Article, QueryCondition
from src.dao.dao import Dao
from src.dao.article_dao import ArticleDao
from src.service.service import Service


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

    def update(self, *args, **kwargs) -> bool: ...

    def remove(self, article_id: int) -> bool:
        if article_id <= 0:
            return False
        else:
            count: int = self.count()
            if article_id > count:
                return False
        return self._dao.remove(article_id)

    def query_one(self, article_id: int) -> Article | None:
        if article_id <= 0:
            return False
        else:
            count: int = self.count()
            if article_id > count:
                return False
        return self._dao.query_one(article_id)

    def query_by_page(self, query_condition: QueryCondition) -> List[Article]:
        return self._dao.query_by_condition(query_condition)

    def get_counts(self) -> int:
        return self._dao.get_counts()

    def get_pages(self, page_size: int = 10) -> int:
        if page_size <= 0:
            return 1
        return self._dao.get_pages(page_size)
