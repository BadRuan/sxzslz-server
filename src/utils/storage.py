from src.utils.logger import Logger
from src.config.configuration import DatabaseConfig, get_database_config
from pymysql import connect, cursors


logger = Logger(__name__)


class Storage:
    def __init__(self):
        self.conn = None

    def _execute(self, sql: str, args: tuple = None):
        cursor = self.conn.cursor()
        cursor.execute("SET time_zone= 'Asia/Shanghai';")  # 解决时区不一致问题
        cursor.execute(sql, args)
        return cursor

    def query_one(self, sql: str, args: tuple = None):
        return self._execute(sql, args).fetchone()

    def query_all(self, sql: str, args: tuple = None):
        return self._execute(sql, args).fetchall()

    def save(self, sql: str, args: tuple = None):
        self._execute(sql, args)
        self.conn.commit()

    def remove(self, sql: str, args: tuple = None):
        self.save(sql, args)

    def update(self, sql: str, args: tuple = None):
        self.save(sql, args)

    def __enter__(self):
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
            return self

        except Exception:
            logger.error(f"MySQL数据库异常: {Exception}")

    def __exit__(self, exc_type, exc, tb):
        self.conn.close()
