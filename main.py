from src.utils.storage import Storage


def main():
    with Storage() as storage:
        sql: str = "SELECT * FROM user"
        result = storage.query(sql)
        for i in result:
            print(i)


if __name__ == "__main__":
    main()
