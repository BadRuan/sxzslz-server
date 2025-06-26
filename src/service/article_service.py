from typing import List
from src.utils.logger import Logger
from src.model import Article
from src.dao.dao import Dao
from src.dao.article_dao import ArticleDao
from src.dao.subset_dao import SubsetDao
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

    def query_by_page(self, subset_id: int, page: int, limit: int) -> List[Article]:
        if subset_id <= 0:
            subset_id = 1
        subsetDao: Dao = SubsetDao()
        counts: int = subsetDao.get_counts()
        if page <= 0 | limit <= 0 | subset_id > counts:
            return []
        pages: int = self.get_pages(limit)
        if page > pages:
            page = pages
        return self._dao.query_by_condition(subset_id, page, limit)
