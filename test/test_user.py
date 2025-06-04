from src.utils.logger import Logger
from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao
from src.service.interface_service import Service
from src.service.subset_service import SubsetService


logger = Logger(__name__)


class TestUser:

    def test_dao_query_all(self):
        dao: Dao = UserDao()
        assert len(dao.query_all()) == dao.count()

    def test_service_query_all(self):
        service: Service = SubsetService()
        assert len(service.query_all()) == service.count()

    def test_dao_query_one(self):
        dao: Dao = UserDao()
        count: int = dao.count()
        logger.debug(dao.query_one(1))
        assert None == dao.query_one(count + 10)
