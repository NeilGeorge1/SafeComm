import socket
from threading import Thread
from RSA import RSA
from db_operations import extract_keys

HOST = "127.0.0.1"
PORT = 55555

running = True
rsa = RSA()

def send(client_socket, other_username):
    global running
    try:
        while running:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                running = False
                print("Exiting chat...")
                client_socket.sendall(message.encode('utf-8'))
                break

            print(f"Sending message to {other_username}...")

            e, d, n = extract_keys(other_username)
            cipher = rsa.encrypt(message, int(e), int(n))

            client_socket.sendall(cipher.encode('utf-8'))
    except BrokenPipeError:
        print("Connection lost. Server might have closed the chat.")
    finally:
        client_socket.close()

def receive(client_socket, username, other_username):
    global running
    try:
        while running:
            cipher = client_socket.recv(1024)
            if cipher == "The user you were talking to has quit. Please type in exit".encode('utf-8'):
                print(cipher.decode('utf-8'))
            elif not cipher:
                break

            e, d, n = extract_keys(username)
            message = rsa.decrypt(cipher.decode('utf-8'), int(d), int(n))

            print(f"Message from {other_username}: {message}")
    except ConnectionResetError:
        print("Server closed the connection.")
    finally:
        running = False
        client_socket.close()

def main(username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall(username.encode('utf-8'))
    other_username = client_socket.recv(1024).decode('utf-8')

    send_thread = Thread(target=send, args=(client_socket, other_username))
    receive_thread = Thread(target=receive, args=(client_socket, username, other_username))

    send_thread.start()
    receive_thread.start()

    send_thread.join()

if __name__ == "__main__":
    username = input("Enter your username: ")
    main(username)
