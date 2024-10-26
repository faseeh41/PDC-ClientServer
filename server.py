import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break  # Connection closed
        print(f"Received: {message.decode()}")
        client_socket.sendall(message)  # Echo the message back to the client
    client_socket.close()

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 connections
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
