from src.utils.logger import Logger
from src.dao.init_database import init_database


logger = Logger(__name__)


def test_init_database():
    init_database()
    logger.debug("执行 init_database 函数")
