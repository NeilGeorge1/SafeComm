import sqlite3 as sql
from hashing import FNV1
from RSA import RSA
import datetime

fnv1 = FNV1() 
rsa = RSA()

def create_user_table():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password INTEGER,
            public_key TEXT,
            private_key TEXT,
            modulus INTEGER
        )
    ''')
    connection.commit()
    connection.close()

def insert_user_values(username, password):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    hashed_password = fnv1.hashReturn(password)

    public_key, private_key, modulus = rsa.generate_keys()
    
    public_key = str(public_key)
    private_key = str(private_key)
    modulus = str(modulus)

    cursor.execute('''
        INSERT INTO users(username, password, public_key, private_key, modulus) VALUES(?, ?, ?, ?, ?)
    ''', (username, hashed_password, public_key, private_key, modulus))

    connection.commit()
    connection.close()

def fetch_user_data():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    for row in data:
        print(row)

    connection.close()

def delete_user_rows(user_id):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    connection.commit()
    connection.close()

def check_user_password(username, password):
    connection = sql.connect('users.db')
    cursor = connection.cursor()
    hash = fnv1.hashReturn(password)

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if str(result[0]) == str(hash):
        return True 
    else:
        return False  

    connection.close()

def extract_keys(username):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("select public_key, private_key, modulus from users where username = ?", (username, ))
    row = cursor.fetchone()

    if row:
        e, d, n = row
        return e, d, n

def create_session_table():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
        create table if not exists sessions(
            session_id INT PRIMARY KEY,
            username  TEXT,
            create_time TEXT,
            logged_in BOOLEAN
        )
    ''')

    connection.commit()
    connection.close()

def insert_session_values(session_id, username):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    logged_in = True

    cursor.execute("INSERT INTO sessions (session_id, username, create_time, logged_in) VALUES (?, ?, ?, ?)",
                   (session_id, username, create_time, logged_in))

    connection.commit()
    connection.close()

def if_logged_in():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("Select logged_in from sessions")
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == 1:
            return True

    return False

    connection.close()

def logout_session(username):
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    logged_in = False
    print(username)
    cursor.execute("update sessions set logged_in = ? where username = ?", (logged_in, username))

    connection.commit()
    connection.close()