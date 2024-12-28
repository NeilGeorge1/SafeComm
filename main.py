from user import login, dashboard, register, logout
from db_operations import if_logged_in, logout_session

def main():
    print("Welcome to SafeComm!")

    while True:
        condition = int(input("Enter command-> Enter 0 for help! "))
        if condition == 0:
            print("Enter 1 for old user")
            print("Enter 2 for new user")
            print("Enter any other key to exit")
        
        elif condition == 1:
            username = login()
            while True:
                if not if_logged_in():
                    username = login()
                else:
                    dashboard(username)
                    break
        elif condition == 2:
            register()
        else:
            break

if __name__ == '__main__':
    main()
