from typing import List
from src.utils.logger import Logger
from src.dao.dao import Dao
from src.dao.subset_dao import SubsetDao
from src.dao.user_dao import UserDao
from src.utils.storage import Storage
from src.model import User, Subset, Article, QueryCondition


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
        sql: str = f"""INSERT INTO `{self.table_name}`
                    (subset_id, user_id, title, content, img_src, state) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        with Storage() as storage:
            storage.save(sql, (subset_id, user_id, title, content, img_src, state))
            return True
        return False

    def update(self, article_id: int, title: str, content: str) -> bool:
        sql: str = f"""UPDATE `{self.table_name}`
                            SET title = %s, content = %s
                            WHERE article_id = '{article_id}'"""
        with Storage() as storage:
            storage.save(sql, (title, content))
            return True
        return False

    def add_read_count(self, article_id: int):
        sql: str = (
            f"UPDATE `{self.table_name}` SET read_count = read_count + 1 WHERE article_id = %s"
        )
        with Storage() as storage:
            storage.save(sql, (article_id,))
            return True
        return False

    def query_one(self, article_id: int) -> Article | None:
        sql: str = f"SELECT * FROM `{self.table_name}` WHERE `article_id` = %s"
        with Storage() as storage:
            result = storage.query_one(sql, (article_id,))
            if result == None:
                return None
            else:
                subset_dao: Dao = SubsetDao()
                user_dao: Dao = UserDao()
                subset: Subset = subset_dao.query_one(result["subset_id"])
                user: User = user_dao.query_one(result["user_id"])
                return Article(
                    article_id=int(result["article_id"]),
                    subset_id=int(result["subset_id"]),
                    user_id=int(result["user_id"]),
                    nick_name=user.nick_name,
                    subset_name=subset.subset_name,
                    title=result["title"],
                    content=result["content"],
                    state=bool(result["state"]),
                    create_time=result["create_time"],
                    read_count=result["read_count"],
                )

    def query_by_condition(self, query_condition: QueryCondition) -> List[Article]:
        offset: int = (query_condition.page - 1) * query_condition.limit
        sql: str = f"SELECT * FROM `{self.table_name}` LIMIT %s, %s"
        with Storage() as storage:
            results = storage.query_all(sql, (offset, query_condition.limit))
            return [
                Article(
                    article_id=int(item["article_id"]),
                    subset_id=int(item["subset_id"]),
                    user_id=int(item["user_id"]),
                    nick_name=None,
                    subset_name=None,
                    title=item["title"],
                    content=None,
                    state=bool(item["state"]),
                    create_time=item["create_time"],
                    read_count=item["read_count"],
                )
                for item in results
            ]
