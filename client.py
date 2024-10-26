import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print(f"Server responded: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    start_client()
