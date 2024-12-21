import socket
from threading import Thread
from RSA import RSA

HOST = "127.0.0.1"
PORT = 55555

def send(client_socket):
    try:
        while True:
            message = input("Enter a message: ")

            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))
    
    except:
        print(f"Error with {client_socket}")

def recieve(client_socket):
    while True:
        message = client_socket.recv(1024)

        if not message:
            break

        print(f"Message recieved: {message.decode('utf-8')}")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    send_thread = Thread(target=send, args=(client_socket, ))
    recieve_thread = Thread(target=recieve, args=(client_socket, ))

    send_thread.start()
    recieve_thread.start()

    send_thread.join()
    print("Chat Ended")

if __name__ == "__main__":
    main()