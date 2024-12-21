import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 55555

def handle_client(client_socket, client_address, other_client_socket):
    try:
        while True:
            message = client_socket.recv(1024)

            if message.decode('utf-8').lower() == 'exit' or not message:
                break

            print(f"Message received from {client_address}")

            other_client_socket.sendall(message)

    except:
        print(f"Error with {client_address}")

    finally:
        client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) #for only two clients at a time

        print("Server Started and listening for incoming clients........")

        client1_socket, client1_address = s.accept()
        print(f"Received client with address: {client1_address}")

        client2_socket, client2_address = s.accept()
        print(f"Received client with address: {client2_address}")

        Thread(target = handle_client, args = (client1_socket, client1_address, client2_socket)).start()
        Thread(target = handle_client, args = (client2_socket, client2_address, client1_socket)).start() 
    
    s.close()

def main():
    start_server()


if __name__ == "__main__":
    main()
     