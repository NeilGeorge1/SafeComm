import sqlite3 as sql
from hashing import FNV1
from RSA import RSA

fnv1 = FNV1() 
rsa = RSA()

def create_table():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password INTEGER,
            public_key INTEGER,
            private_key INTEGER
        )
    ''')
    connection.commit()
    connection.close()

def insert_values(username, password):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    hashed_password = fnv1.hashReturn(password)

    public_key, private_key = rsa.generate_keys()

    cursor.execute('''
        INSERT INTO users(username, password, public_key, private_key) VALUES(?, ?, ?, ?)
    ''', (username, hashed_password, public_key, private_key))

    connection.commit()
    connection.close()

def fetch_data():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    for row in data:
        print(row)

    connection.close()

def delete_rows(user_id):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    connection.commit()
    connection.close()

def check_password(username, password):
    connection = sql.connect('users.db')
    cursor = connection.cursor()
    hash = fnv1.hashReturn(password)

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    # If a result is returned, compare the stored password with the input hash
    if str(result[0]) == str(hash):
        return True  # Password matches
    else:
        return False  # Password does not match or username not found

    # Close the connection
    connection.close()
