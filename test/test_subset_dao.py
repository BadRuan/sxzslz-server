from src.dao.interface_dao import Dao
from src.dao.subset_dao import SubsetDao


class TestSubsetDao:

    def test_query_all(self):
        dao: Dao = SubsetDao()
        assert len(dao.query_all()) == dao.count()
