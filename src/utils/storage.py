from src.utils.logger import Logger
from src.config.configuration import DatabaseConfig, get_database_config
from pymysql import connect, cursors


logger = Logger(__name__)


class Storage:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def _get_conn(self):
        try:
            config: DatabaseConfig = get_database_config()
            self.conn = connect(
                host=config.url,
                port=config.port,
                user=config.user,
                password=config.password,
                database=config.database,
                charset="utf8mb4",
                cursorclass=cursors.DictCursor,
            )
            logger.debug("MySQL数据库连接成功")
            return self.conn

        except Exception:
            logger.error(f"MySQL数据库异常: {Exception}")

    def query(self, sql: str):
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __enter__(self):
        self._get_conn()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.cursor.close()
        self.conn.close()
