from typing import List
from src.utils.storage import Storage
from src.dao.interface_dao import Dao
from src.model import SubsetType, Subset


table_name: str = "subset"
primary_key_name: str = "subset_id"


class SubsetDao(Dao):

    def __init__(self):
        super().__init__(table_name, primary_key_name)

    def add(
        self,
        subset_name: str,
        subset_type: SubsetType,
    ) -> bool:
        sql: str = f"""INSERT INTO `{self.table_name}` (
                        subset_name,  subset_type
                        ) VALUES (
                        '%s', %s
                        )"""
        with Storage() as storage:
            storage.save(sql, (subset_name, subset_type.value))
            return True
        return False

    def update(self, subset_id: int, subset_name: str) -> bool:
        sql: str = (
            f"""UPDATE `{self.table_name}`
                        SET subset_name = '%s'
                        WHERE subset_id = '%s"""
        )
        with Storage() as storage:
            storage.update(sql, (subset_name, subset_id))
            return True
        return False

    def query_one(self, subset_id: int) -> Subset | None:
        sql: str = f"SELECT * FROM `{self.table_name}` WHERE subset_id = '%s'"
        with Storage() as storage:
            result = storage.query_one(sql, (subset_id))
            if result == None:
                return None
            else:
                return Subset(
                    subset_id=int(result["subset_id"]),
                    subset_name=result["subset_name"],
                    subset_type=SubsetType(result["subset_type"]),
                    create_time=result["create_time"],
                )

    def query_by_page(self, page: int, limit: int) -> List[Subset]:
        offset: int = (page - 1) * limit
        sql: str = f"SELECT * FROM {self.table_name} LIMIT %s, %s"
        with Storage() as storage:
            results = storage.query_all(sql, (offset, limit))
            return [
                Subset(
                    subset_id=int(item["subset_id"]),
                    subset_name=item["subset_name"],
                    subset_type=SubsetType(item["subset_type"]),
                    create_time=item["create_time"],
                )
                for item in results
            ]

    def query_all(self) -> List[Subset]:
        sql: str = f"SELECT * FROM `{self.table_name}`"
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                Subset(
                    subset_id=int(item["subset_id"]),
                    subset_name=item["subset_name"],
                    subset_type=SubsetType(item["subset_type"]),
                    create_time=item["create_time"],
                )
                for item in results
            ]

    def query_by_condition(
        self, subset_type: SubsetType, page: int, limit: int
    ) -> List[Subset]:
        offset: int = (page - 1) * limit
        sql: str = (
            f"SELECT * FROM `{self.table_name}` WHERE `subset_type`={subset_type.value}  LIMIT %s, %s"
        )
        with Storage() as storage:
            results = storage.query_all(sql, (offset, limit))
            return [
                Subset(
                    subset_id=int(item["subset_id"]),
                    subset_name=item["subset_name"],
                    subset_type=SubsetType(item["subset_type"]),
                    create_time=item["create_time"],
                )
                for item in results
            ]
