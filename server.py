import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 55555

client_dict= {}#username in bytes

def handle_client(client_socket, client_address, other_client_socket):
    try:
        while True:
            message = client_socket.recv(1024)

            if message.decode('utf-8').lower() == 'exit' or not message:
                break

            print(f"{message} received from Username: {client_dict[client_socket]}, Address:{client_address}")

            other_client_socket.sendall(message)

    except:
        print(f"Error with {client_address}")

    finally:
        client_socket.close()
        other_client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) 

        print("Server Started and listening for incoming clients........")

        client1_socket, client1_address = s.accept()
        print(f"Received client1 with address: {client1_address}")

        client2_socket, client2_address = s.accept()
        print(f"Received client2 with address: {client2_address}")

        #first recieve usernames
        username1 = client1_socket.recv(1024)
        username2 = client2_socket.recv(1024)

        #adding them to dict
        client_dict[client1_socket] = username1
        client_dict[client2_socket] = username2

        #sending the username to other client for rsa
        client2_socket.sendall(client_dict[client1_socket])
        client1_socket.sendall(client_dict[client2_socket])

        Thread(target = handle_client, args = (client1_socket, client1_address, client2_socket)).start()
        Thread(target = handle_client, args = (client2_socket, client2_address, client1_socket)).start() 
    
    s.close()

def main():
    start_server()


if __name__ == "__main__":
    main()
     