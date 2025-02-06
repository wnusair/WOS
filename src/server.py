import socket
import threading
import sys
import os

# Add the src folder to the system path (modify as needed for your project structure)
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from wissampy import print_message

def send_file(client_socket, file_path):
    """
    Send the entire file to the client.
    If the file doesn't exist, just print an error and close.
    """
    if not os.path.isfile(file_path):
        # You can choose to send an error message to client, or do nothing
        print_message(f"File not found: {file_path}", "INTERNET")
        return

    try:
        with open(f"{file_path}", 'rb') as f:
            data = f.read()
            client_socket.sendall(data)
        print_message(f"Sent file '{file_path}' to client.", "INTERNET")
    except Exception as e:
        print_message(f"Failed to send file '{file_path}': {e}", "INTERNET")

def handle_client(client_socket, client_address):
    """
    Handle a single client connection in a separate thread.
    1. Read the file name requested by the client.
    2. Attempt to send that file.
    3. Close the connection.
    """
    print_message(f"Client {client_address} connected.", "INTERNET")

    try:
        # Wait for the client to send the file name (up to 1024 bytes)
        data = client_socket.recv(1024).decode('utf-8').strip()

        if data == "UPDATE":
            print_message(f"Client {client_address} requested an update.", "INTERNET")
            # Receive the file data until the client closes
            with open("files/apps.csv", 'ab') as f:
                while True:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    f.write(data)
            print_message(f"Updated 'apps.csv' from client {client_address}.", "INTERNET")
        elif data == "UPLOAD":
            print_message(f"Client {client_address} is uploading a file.", "INTERNET")

            # recv file info
            file_name = client_socket.recv(1024).decode('utf-8').strip()

            # Receive the file data until the client closes
            with open(f"apps/{file_name}", 'wb') as f:
                while True:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    f.write(data)
            
            print_message(f"Uploaded '{file_name}' from client {client_address}.", "INTERNET")

        if data:
            file_name = data  # The client is requesting this file
            print_message(f"Client {client_address} requested '{file_name}'.", "INTERNET")

            send_file(client_socket, file_name)
    except Exception as e:
        print_message(f"Error handling client {client_address}: {e}", "INTERNET")
    finally:
        client_socket.close()
        print_message(f"Client {client_address} disconnected.", "INTERNET")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to all interfaces on port 5555
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)

    print_message("Server is listening on port 5555...", "INTERNET")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            # Create a new thread to handle this client
            t = threading.Thread(target=handle_client, args=(client_socket, client_address))
            t.start()
    except KeyboardInterrupt:
        print_message("Server shutting down...", "INTERNET")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
