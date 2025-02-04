import socket
import threading
import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# Now you can import wissampy
import wissampy

HOST = "localhost"
PORT = 55000
BUFFER_SIZE = 1024

def handle_client(client_socket) -> None:
    """ Handles a single client connection """
    try:
        while True:
            # Receive message from the client
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            
            if not message:  # If no data, break connection
                break

            # Print the received message
            wissampy.print_message(f"Received message: {message}", "INFO")

            # Echo the message back to the client
            response = f"Server received: {message}"
            client_socket.sendall(response.encode('utf-8'))

    except Exception as e:
        wissampy.print_message(f"Error: {e}", "ERROR")
    finally:
        client_socket.close()

def start_server() -> None:
    """ Starts the server """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    wissampy.print_message(f"Server is listening on {HOST}:{PORT}", "INTERNET")

    while True:
        client_socket, addr = server.accept()
        wissampy.print_message(f"Accepted connection from {addr}", "INTERNET")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    # project_name, description, author, created_at, updated_at, size
    wissampy.create_db("apps.csv", ["name", "description", "author", "created_at", "updated_at", "size"])
    wissampy.print_message("Welcome to WOS-Server-Alpha", "SUCCESS")
    start_server()