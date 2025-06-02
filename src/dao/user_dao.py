from typing import List
from src.utils.logger import Logger
from src.dao.interface_dao import Dao
from src.utils.storage import Storage


logger = Logger(__name__)


class UserDao(Dao):

    def add(
        self, user_name: str, nick_name: str, password: str, avatar_src: str
    ) -> bool:
        sql: str = f"""INSERT INTO `user`
                    (user_name, nick_name, password, avatar_src, create_time)
                    VALUES
                    ('{user_name}', '{nick_name}', '{password}', '{avatar_src}', NOW() )"""
        with Storage() as storage:
            storage.save(sql)
            return True
        return False

    def remove(self, user_id: int) -> bool:
        sql: str = f"DELETE FROM `user` WHERE user_id = '{user_id}'"
        with Storage() as storage:
            storage.remove(sql)
            return True
        return False

    def update(self, user_id: int, new_hashed_password: str) -> bool:
        sql: str = f"""UPDATE `user`
                        SET password = '{new_hashed_password}'
                        WHERE user_id = '{user_id}'"""
        with Storage() as storage:
            storage.update(sql)
            return True
        return False

    def query_one(self, user_id: int):
        sql: str = f"SELECT * FROM `user` WHERE `user_id` = {user_id}"
        with Storage() as storage:
            results = storage.query_one(sql)
            return results

    def query_all(self) -> List:
        sql: str = "SELECT * FROM `user`"
        with Storage() as storage:
            results = storage.query_all(sql)
            return results

    def count(self) -> int:
        sql: str = "SELECT COUNT(*) AS 'count' FROM `user`"
        with Storage() as storage:
            result = storage.query_one(sql)
            return result["count"]
