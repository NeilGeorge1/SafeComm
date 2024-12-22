from db_operations import create_table, insert_values, fetch_data, delete_rows, check_password
from time import sleep

def main():
    create_table()

    print("Welcome to SafeComm!")
    print("Type 0 for help")

    while True:

        condition = int(input("Enter command-> "))

        if condition == 0:
            print("Enter 1 for old user")
            print("Enter 2 for new user")
            print("Enter any other key to exit")
        
        elif condition == 1:
            username = input("Enter Username-> ")
            password = input("Enter Password-> ")

            print("Authenticating......")
            sleep(2)

            if check_password(username, password) == True:
                print("Authenticated!")
                print("Welcome!!")
                print(":)")
            
            else:
                print("Invalid Credentials")
                print("Please Try Again")
        
        elif condition == 2:
            print("Please enter your credentials-> ")
            username = input("Enter Username-> ")
            password = input("Enter Password-> ")

            insert_values(username, password)

            print("Succesfully made a new account!")
            print("Please Log in")

        else:
            break

if __name__ == '__main__':
    main()
