import socket
import threading
from RSA import RSA
from threading import Thread
from db_operations import extract_keys

HOST = "13.51.178.218"
PORT = 55555

lock = threading.Lock()
rsa = RSA()

def send(client_socket, other_username):
    while True:
        message = input("Enter a message: ")
        print(f"Sending message to {other_username}......")

        if message.lower() == 'exit':
            break

        e, d, n = extract_keys(other_username)
        e = int(e)
        d = int(d)
        n = int(n)
        cipher = rsa.encrypt(message, e ,n)
        #sleep(1)

        client_socket.sendall(cipher.encode('utf-8'))

def recieve(client_socket, username, other_username):
    while True:
        cipher = client_socket.recv(1024)
        cipher = cipher.decode('utf-8')

        e, d, n = extract_keys(username)
        e = int(e)
        d = int(d)
        n = int(n)
        message = rsa.decrypt(cipher, d, n)

        if not message:
            break

        print(f"Message recieved from {other_username}: {message}")

def main(username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    #sending username
    client_socket.sendall(username.encode('utf-8'))

    #recieving other username
    other_username = client_socket.recv(1024)
    other_username = other_username.decode('utf-8')

    send_thread = Thread(target=send, args=(client_socket, other_username))
    recieve_thread = Thread(target=recieve, args=(client_socket, username, other_username))

    send_thread.start()
    recieve_thread.start()

    send_thread.join()
    recieve_thread.join()

    print("Chat Ended")

if __name__ == "__main__":
    main(username)