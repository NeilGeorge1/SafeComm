import sqlite3 as sql
from datetime import datetime, timedelta

session_time = 5

def cleanup():
    connection = sql.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("select create_time, username, logged_in from sessions")
    rows = cursor.fetchall()

    for row in rows:

        datetime_string = row[0]
        datetime_object = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')

        if datetime_object - datetime.now() <= timedelta(minutes=5) and row[2] == True:
            print(f"Session for {row[1]} has been closed")
            cursor.execute("update sessions set logged_in = ? where username = ?", (False, row[1],))
        
    connection.commit()
    connection.close()

cleanup()
print(1)