from typing import List
from src.utils.storage import Storage
from src.dao.interface_dao import Dao
from src.model import SubsetType, SubsetModel


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

    def update(self, subset_id: int, subset_name: str) -> bool:
        sql: str = (
            """UPDATE `%s`
                        SET subset_name = '%s'
                        WHERE subset_id = '%s"""
            % (self.table_name, subset_name, subset_id)
        )
        with Storage() as storage:
            storage.update(sql)
            return True
        return False

    def query_one(self, subset_id: int) -> SubsetModel | None:
        sql: str = f"SELECT * FROM `%s` WHERE subset_id = '%s'" % (
            self.table_name,
            subset_id,
        )
        with Storage() as storage:
            result = storage.query_one(sql)
            if result == None:
                return None
            else:
                return SubsetModel(
                    subset_id=int(result["subset_id"]),
                    subset_name=result["subset_name"],
                    subset_type=SubsetType(result["subset_type"]),
                    create_time=result["create_time"],
                )

    def query_by_page(self, page: int, limit: int) -> List[SubsetModel]:
        offset: int = (page - 1) * limit
        sql: str = "SELECT * FROM %s LIMIT %s, %s" % (self.table_name, offset, limit)
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                SubsetModel(
                    subset_id=int(item["subset_id"]),
                    subset_name=item["subset_name"],
                    subset_type=SubsetType(item["subset_type"]),
                    create_time=item["create_time"],
                )
                for item in results
            ]

    def query_all(self) -> List[SubsetModel]:
        sql: str = "SELECT * FROM `%s`" % self.table_name
        with Storage() as storage:
            results = storage.query_all(sql)
            return [
                SubsetModel(
                    subset_id=int(item["subset_id"]),
                    subset_name=item["subset_name"],
                    subset_type=SubsetType(item["subset_type"]),
                    create_time=item["create_time"],
                )
                for item in results
            ]
