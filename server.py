import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 55555

def handle_client(client_socket, client_address, other_client_socket):
    try:
        while True:
            message = client_socket.recv(1024)

            if not message or message.decode('utf-8').lower() == 'exit':
                print(f"Client {client_address} disconnected.")
                other_client_socket.sendall("The user you were talking to has quit. Please type in exit".encode('utf-8'))
                other_client_socket.close()
                client_socket.close()
                return 

            print(f"Received: {message.decode('utf-8')} from {client_address}")
            other_client_socket.sendall(message)
    except (ConnectionResetError, BrokenPipeError):
        print(f"Connection lost with {client_address}.")
        other_client_socket.close()
        client_socket.close()

def start_server():
    while True: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(2)

            print("Server is waiting for two users...")

            client1_socket, client1_address = s.accept()
            print(f"Client 1 connected: {client1_address}")

            client2_socket, client2_address = s.accept()
            print(f"Client 2 connected: {client2_address}")

            username1 = client1_socket.recv(1024)
            username2 = client2_socket.recv(1024)

            client2_socket.sendall(username1)
            client1_socket.sendall(username2)

            Thread(target=handle_client, args=(client1_socket, client1_address, client2_socket)).start()
            Thread(target=handle_client, args=(client2_socket, client2_address, client1_socket)).start()

def main():
    start_server()

if __name__ == "__main__":
    main()
