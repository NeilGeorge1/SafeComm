from db_operations import create_table, insert_values, fetch_data, delete_rows

def main():
    create_table()

    username = "john_doe"
    password = "password123"
    insert_values(username, password)

    fetch_data()

    delete_rows(1)

if __name__ == '__main__':
    main()
