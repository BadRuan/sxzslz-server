from typing import List
from src.utils.logger import Logger
from src.model import User
from src.dao.dao import Dao
from src.dao.user_dao import UserDao
from src.service.service import Service
from src.service.user_service import UserService


logger = Logger(__name__)


class TestUser:

    def test_dao_get_pages(self):
        dao: Dao = UserDao()
        limit: int = 10
        pages: int = dao.get_pages(limit)
        assert pages > 0

    def test_dao_get_counts(self):
        dao: Dao = UserDao()
        counts: int = dao.get_counts()
        assert counts >= 0

    def test_dao_query_one(self):
        dao: Dao = UserDao()
        id: int = 1
        u: User = dao.query_one(id)
        assert u != None

    def test_dao_query_condition(self):
        dao: Dao = UserDao()
        page, limit = 1, 20
        results: List[User] = dao.query_by_condition(page, limit)
        assert len(results) > 0

    def test_service_get_counts(self):
        service: Service = UserService()
        counts: int = service.get_counts()
        assert counts >= 0

    def test_service_get_pages(self):
        service: Service = UserService()
        limit: int = 10
        pages: int = service.get_pages(limit)
        assert pages > 0

    def test_service_query_by_page(self):
        service: Service = UserService()
        page, limit = 1, 20
        results: List[User] = service.query_by_page(page, limit)
        assert len(results) > 0

    def test_service_add_user(self):
        service: Service = UserService()
        result: bool = service.add(
            user_name="", nick_name="", password="", avatar_src=""
        )
        assert result == False
        result = service.add(user_name="", nick_name="", password="", avatar_src="saf")
        assert result == False
