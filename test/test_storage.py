from src.utils.logger import Logger
from src.utils.storage import Storage

logger = Logger(__name__)


class TestStorage:

    def test_storage(self):
        sql: str = "SELECT * FROM`user` where user_id = %s"
        with Storage() as storage:
            results = storage.query_all(sql, ("1"))
            for i in results:
                logger.debug(i)
