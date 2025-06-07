from typing import List
from src.utils.logger import Logger
from src.dao.interface_dao import Dao
from src.utils.storage import Storage
from src.model import ArticleModel


table_name: str = "article"
primary_key_name: str = "article_id"
logger = Logger(__name__)


class ArticleDao(Dao):

    def __init__(self):
        super().__init__(table_name, primary_key_name)

    def add(
        self,
        subset_id: int,
        user_id: int,
        title: str,
        content: str,
        img_src: str,
        state: bool,
    ) -> bool:
        sql: str = f"""INSERT INTO `{self.table_name}` (
                        subset_id, user_id, title, content, img_src, state, create_time
                        ) VALUES (
                        '%s', '%s', '%s', '%s', '%s', %s, now()
                        )"""
        logger.debug(f"Article Add SQL: {sql}")
        with Storage() as storage:
            storage.save(sql, (subset_id, user_id, title, content, img_src, state))
            return True
        return False

    def update(self, *args, **kwargs) -> bool: ...

    def query_one(self, article_id: int) -> ArticleModel | None:
        sql: str = f"SELECT * FROM `{self.table_name}` WHERE `article_id` = %s"
        with Storage() as storage:
            result = storage.query_one(sql, (article_id,))
            if result == None:
                return None
            else:
                return ArticleModel(
                    article_id=int(result["article_id"]),
                    subset_id=int(result["subset_id"]),
                    user_id=int(result["user_id"]),
                    title=result["title"],
                    content=result["content"],
                    state=bool(result["state"]),
                    create_time=result["create_time"],
                    read_count=int(result["read_count"]),
                )

    def query_by_page(self, page: int, limit: int) -> List[ArticleModel]:
        offset: int = (page - 1) * limit
        sql: str = f"SELECT * FROM `{self.table_name}` LIMIT %s, %s"
        with Storage() as storage:
            results = storage.query_all(sql, (offset, limit))
            return [
                ArticleModel(
                    article_id=int(item["article_id"]),
                    subset_id=int(item["subset_id"]),
                    user_id=int(item["user_id"]),
                    title=item["title"],
                    # content=item["content"],
                    content=None,
                    state=bool(item["state"]),
                    create_time=item["create_time"],
                    read_count=int(item["read_count"]),
                )
                for item in results
            ]

    def query_all(self) -> List[ArticleModel]:
        sql: str = f"SELECT * FROM `{self.table_name}`"
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                ArticleModel(
                    article_id=int(item["article_id"]),
                    subset_id=int(item["subset_id"]),
                    user_id=int(item["user_id"]),
                    title=item["title"],
                    content=item["content"],
                    state=bool(item["state"]),
                    create_time=item["create_time"],
                    read_count=int(item["read_count"]),
                )
                for item in results
            ]
