from src.utils.storage import Storage
from typing import List
from src.dao.interface_dao import Dao
from src.model import SubsetType


class SubsetDao(Dao):

    def add(
        self,
        subset_name: str,
        subset_type: SubsetType,
    ) -> bool:
        sql: str = f"""INSERT INTO `subset` (
                        subset_name, 
                        subset_type
                        ) VALUES (
                        '{subset_name}', 
                        {subset_type.value}
                        )"""
        with Storage() as storage:
            storage.save(sql)
            return True
        return False

    def remove(self, subset_id: int) -> bool:
        sql: str = f"DELETE FROM `subset` WHERE subset_id = '{subset_id}'"
        with Storage() as storage:
            storage.remove(sql)
            return True
        return False

    def update(self, subset_id: int, subset_name: str) -> bool:
        sql: str = f"""UPDATE `subset`
                        SET subset_name = '{subset_name}'
                        WHERE subset_id = '{subset_id}"""
        with Storage() as storage:
            storage.update(sql)
            return True
        return False

    def query_one(self, subset_id: int):
        sql: str = f"SELECT * FROM `subset` WHERE subset_id = '{subset_id}"
        with Storage() as storage:
            results = storage.query_all(sql)
            return results
        return []

    def query_all(self) -> List:
        sql: str = "SELECT * FROM `subset`"
        with Storage() as storage:
            results = storage.query_all(sql)
            return results
        return []

    def count(self) -> int:
        sql: str = "SELECT COUNT(*) AS 'count' FROM `subset`"
        with Storage() as storage:
            result = storage.query_one(sql)
            return result["count"]
        return 0
