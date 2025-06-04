from typing import List
from src.service.interface_service import Service
from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao
from src.model import UserModel


class UserService(Service):

    def __init__(self):
        super().__init__()
        self._dao: Dao = UserDao()

    def add(
        self, user_name: str, nick_name: str, password: str, avatar_src: str
    ) -> bool:
        return self._dao.add(user_name, nick_name, password, avatar_src)

    def remove(self, user_id: int) -> bool:
        return self._dao.remove(user_id)

    def update(self, user_id: int, new_hashed_password: str) -> bool:
        return self._dao.update(user_id, new_hashed_password)

    def query_one(self, user_id: int) -> UserModel | None:
        return self._dao.query_one(user_id)

    def query_by_page(self, page: int, limit: int) -> List[UserModel]:
        return self._dao.query_by_page(page, limit)

    def query_all(self) -> List[UserModel]:
        return self._dao.query_all()

    def count(self) -> int:
        return self._dao.count()

    def pages(self, page_size: int = 10) -> int:
        return self._dao.pages(page_size)
