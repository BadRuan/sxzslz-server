from typing import List
from src.utils.logger import Logger
from src.model import User
from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao
from src.service.interface_service import Service
from src.service.user_service import UserService


logger = Logger(__name__)


class TestUser:

    def test_query_all(self):
        dao: Dao = UserDao()
        service: Service = UserService()
        assert len(dao.query_all()) == dao.count()
        assert len(service.query_all()) == service.count()

    def test_query_by_page(self):
        dao: Dao = UserDao()
        page, limit = 1, 10
        results: List[User] = dao.query_by_page(page, limit)
        assert len(results) > 0

    def test_query_one(self):
        dao: Dao = UserDao()
        service: Service = UserService()
        count: int = dao.count()
        assert None == dao.query_one(count + 10)
        count = service.count()
        assert None == service.query_one(count + 10)
