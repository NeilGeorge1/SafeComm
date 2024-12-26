from db_operations import insert_user_values, fetch_user_data, delete_user_rows, check_user_password, insert_session_values, if_logged_in, logout_session
from time import sleep
import getpass
import secrets
import string   

def generate_session_id():
    return secrets.token_hex(16)

def login():
    username = input("Enter Username-> ")
    password = getpass.getpass("Enter your password: ")

    print("Authenticating......")
    sleep(2)

    if check_user_password(username, password) == True:
        print("Authenticated!")
        print(f"Welcome {username.split(' ')[0]}!!")
        print(":)")

        insert_session_values(generate_session_id(), username)
            
    else:
        print("Invalid Credentials")
        print("Please Try Again")

    return username

def dashboard(username):
    number = int(input("Enter 0 to print hello, print 1 to logout-> "))
    if number == 0:
        print("Hello ")
    elif number == 1:
        logout(username)
    else:
        print("Invalid Request")

def logout(username):
    print("Logging out.......")
    sleep(1)
    logout_session(username)

def register():
    print("Please enter your credentials-> ")
    while True:
        username = input("Enter Username-> ")
        password = getpass.getpass("Enter your password: ")
        password_confirm = getpass.getpass("Confirm your password: ")

        if password != password_confirm:
            print("The password is not the same. Please try again")
        else:
            break

    insert_user_values(username, password)

    print("Succesfully made a new account!")
    print("Please Log in")

