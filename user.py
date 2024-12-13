import sqlite3 as sql
from RSA import RSA 

rsa = RSA()

class User:
    id = 0

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def create_table(self):
        connection = sql.connect('users.db')
        cursor = connection.cursor()

        cursor.execute ('''
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                public_key INTEGER,
                private_key INTEGER
            )
        '''
        )
        connection.commit()
        connection.close()

    def insert_values(self):
        connection = sql.connect('users.db')
        cursor = connection.cursor()

        #id += 1
        cursor.execute('''
            INSERT INTO users(user_id, username, password, public_key, private_key) VALUES(?, ?, ?, ?, ?)
        '''
        , (1, self.username, self.password, rsa.generate_keys()[0], rsa.generate_keys()[1])
        )

        connection.commit()
        connection.close()

    def fetch_data(self):
        connection = sql.connect('users.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        for row in data:
            print(row)

        connection.close()

    def delete_rows(self, id):
        connection = sql.connect('users.db')
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE user_id = ?", (id,))
        connection.commit()
        connection.close()


user1 = User('neil', 'qwerty')

user1.create_table()
user1.insert_values()
user1.fetch_data()
user1.delete_rows(1)