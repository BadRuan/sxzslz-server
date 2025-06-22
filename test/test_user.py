from typing import List
from src.utils.logger import Logger
from src.model import User, QueryCondition
from src.dao.dao import Dao
from src.dao.user_dao import UserDao
from src.service.service import Service
from src.service.user_service import UserService


logger = Logger(__name__)


class TestUser:

    def test_dao_query_by_page(self):
        dao: Dao = UserDao()
        query_condition: QueryCondition = QueryCondition(page=1, limit=20, onther=None)
        results: List[User] = dao.query_by_condition(query_condition)
        assert len(results) > 0
        logger.debug(f"Dao层 User对象  查询用户数据运行成功")

    def test_service_count_and_pages(self):
        service: Service = UserService()
        count: int = service.get_counts()
        pages: int = service.get_pages()
        logger.debug(f"Service层 User对象 查询用户总数运行成功，共{count}个用户")

    def test_service_query_by_page(self):
        service: Service = UserService()
        pagination_condition: QueryCondition = QueryCondition(
            page=1, limit=20, onther=None
        )
        results: List[User] = service.query_by_page(pagination_condition)
        assert len(results) > 0
        logger.debug(f"Service层 User对象 批量查询用户数据运行成功")

    def test_service_add_user(self):
        service: Service = UserService()
        result: bool = service.add(
            user_name="", nick_name="", password="", avatar_src=""
        )
        assert result == False
        result = service.add(user_name="", nick_name="", password="", avatar_src="saf")
        assert result == False
