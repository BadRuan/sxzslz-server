from typing import List
from src.model import User, QueryCondition
from src.dao.dao import Dao
from src.dao.user_dao import UserDao
from src.service.service import Service


class UserService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = UserDao()

    def add(
        self, user_name: str, nick_name: str, password: str, avatar_src: str
    ) -> bool:
        def is_not_empty(item: str):
            if item.strip() == "":
                return False
            return True

        def any_not_empty(lst):
            return all(is_not_empty(item) for item in lst)

        if any_not_empty([user_name, nick_name, password, avatar_src]):
            return self._dao.add(user_name, nick_name, password, avatar_src)
        else:
            return False

    def remove(self, user_id: int) -> bool:
        if user_id <= 0:
            return False
        else:
            count: int = self.get_counts()
            if user_id > count:
                return False
        return self._dao.remove(user_id)

    def update(self, user_id: int, new_hashed_password: str) -> bool:
        if user_id <= 0:
            return False
        else:
            count: int = self.get_counts()
            if user_id > count:
                return False
        return self._dao.update(user_id, new_hashed_password)

    def query_one(self, user_id: int) -> User | None:
        if user_id <= 0:
            return None
        else:
            count: int = self.get_counts()
            if user_id > count:
                return None
        return self._dao.query_one(user_id)

    def query_by_page(self, query_condition: QueryCondition) -> List[User]:
        return self._dao.query_by_condition(query_condition)

    def get_counts(self) -> int:
        return self._dao.get_counts()

    def get_pages(self, page_size: int = 10) -> int:
        if page_size <= 0:
            return 1
        return self._dao.get_pages(page_size)
