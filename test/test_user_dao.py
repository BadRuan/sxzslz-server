from src.dao.user_dao import UserDao
from pytest import fixture


class TestUserDao:

    def test_select_all_user(self):
        dao = UserDao()
        assert len(dao.select_all_user()) == dao.get_total_user_count()
