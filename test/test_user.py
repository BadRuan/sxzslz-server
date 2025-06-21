from typing import List
from src.utils.logger import Logger
from src.model import User, QueryCondition
from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao


logger = Logger(__name__)


class TestUser:

    def test_query_by_page(self):
        dao: Dao = UserDao()
        pagination_condition: QueryCondition = QueryCondition(
            page=1, limit=20, onther=None
        )
        results: List[User] = dao.query_by_condition(pagination_condition)
        assert len(results) > 0
