from src.dao.user_dao import UserDao


def main():
    dao = UserDao()
    result = dao.select_all_user()
    print(result)


if __name__ == "__main__":
    main()
