from typing import List
from src.dao.interface_dao import Dao
from src.utils.storage import Storage
from src.model import UserModel
from src.utils.logger import Logger

# table_name: str = "user"
# primary_key_name: str = "user_id"
logger = Logger(__name__)


class UserDao(Dao):

    def __init__(self):
        super().__init__("user", "user_id")

    def add(
        self, user_name: str, nick_name: str, password: str, avatar_src: str
    ) -> bool:
        sql: str = f"""INSERT INTO `{self.table_name}`
                    (user_name, nick_name, password, avatar_src, create_time)
                    VALUES
                    ('{user_name}', '{nick_name}', '{password}', '{avatar_src}', NOW() )"""
        with Storage() as storage:
            storage.save(sql)
            return True
        return False

    def update(self, user_id: int, new_hashed_password: str) -> bool:
        sql: str = (
            """UPDATE `%s`
                        SET password = '%s'
                        WHERE user_id = '%s'"""
            % (self.table_name, new_hashed_password, user_id)
        )
        with Storage() as storage:
            storage.update(sql)
            return True
        return False

    def query_one(self, user_id: int) -> UserModel | None:
        sql: str = "SELECT * FROM `%s` WHERE `user_id` = %s" % (
            self.table_name,
            user_id,
        )
        with Storage() as storage:
            result = storage.query_one(sql)
            if result == None:
                return None
            else:
                return UserModel(
                    user_id=int(result["user_id"]),
                    user_name=result["user_name"],
                    nick_name=result["nick_name"],
                    password=result["password"],
                    avatar_src=result["avatar_src"],
                    create_time=result["create_time"],
                )

    def query_by_page(self, page: int, limit: int) -> List[UserModel]:
        offset: int = (page - 1) * limit
        sql: str = "SELECT * FROM %s LIMIT %s, %s" % (self.table_name, offset, limit)
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                UserModel(
                    user_id=int(item["user_id"]),
                    user_name=item["user_name"],
                    nick_name=item["nick_name"],
                    password=item["password"],
                    avatar_src=item["avatar_src"],
                    create_time=item["create_time"],
                )
                for item in results
            ]

    def query_all(self) -> List[UserModel]:
        sql: str = "SELECT * FROM `%s`" % (self.table_name)
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                UserModel(
                    user_id=int(item["user_id"]),
                    user_name=item["user_name"],
                    nick_name=item["nick_name"],
                    password=item["password"],
                    avatar_src=item["avatar_src"],
                    create_time=item["create_time"],
                )
                for item in results
            ]
