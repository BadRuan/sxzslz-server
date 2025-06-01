from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao
from src.dao.subset_dao import SubsetDao


def main():
    dao: Dao = SubsetDao()
    count = dao.count()
    print(f"count: {count}")
    result = dao.query_all()
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
