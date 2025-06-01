from src.utils.logger import Logger
from src.utils.storage import Storage
from typing import List

logger = Logger(__name__)


class UserDao:

    def add_user(self, user_name: str, nick_name: str, password: str, avatar_src: str):
        sql: str = f"""
INSERT INTO `user`
(user_name, nick_name, password, avatar_src, create_time)
VALUES
('{user_name}', '{nick_name}', '{password}', '{avatar_src}', NOW() )"""
        with Storage() as storage:
            storage.save_data(sql)

    def remove_user(self, user_id: int):
        sql: str = f"DELETE FROM `user` WHERE user_id = '{user_id}'"
        with Storage() as storage:
            storage.save_data(sql)

    def update_user_password(self, user_id: int, new_hashed_password: str):
        sql: str = f"""
UPDATE `user`
SET password = '{new_hashed_password}'
WHERE user_id = '{user_id}'"""
        with Storage() as storage:
            storage.save_data(sql)

    def select_all_user(self) -> List:
        sql: str = "SELECT * FROM `user`"
        with Storage() as storage:
            results = storage.query_all(sql)
            return results

    def get_total_user_count(self) -> int:
        sql: str = "SELECT COUNT(*) AS 'total_users' FROM `user`"
        with Storage() as storage:
            result = storage.query_one(sql)
            return result["total_users"]
