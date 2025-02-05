import socket
import sys
import os

# Adjust path as necessary for your project
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from wissampy import print_message

def download_file(server_host, server_port, remote_file, local_file):
    """
    Connect to the specified server, request `remote_file`,
    and save it locally as `local_file`.

    Usage example:
        from client_module import download_file
        download_file('127.0.0.1', 5555, 'test/apps.csv', 'apps.csv')
    """
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print_message(f"Connected to server at {(server_host, server_port)}", "INTERNET")

        # Send the file name we want
        client_socket.sendall(remote_file.encode('utf-8'))

        # Receive the file data until the server closes
        with open(local_file, 'wb') as f:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                f.write(data)

        print_message(f"Downloaded '{remote_file}' to '{local_file}'.", "INTERNET")

    except Exception as e:
        print_message(f"Error downloading file '{remote_file}': {e}", "INTERNET")
    finally:
        client_socket.close()
        print_message("Connection closed.", "INTERNET")

def update_csv(server_host, server_port, remote_file):
    project_name = input("Enter the project name: ")
    project_version = input("Enter the project version: ")
    project_description = input("Enter the project description: ")
    project_developer = input("Enter the project developer: ")
    project_path = input("Enter the project path: ")

    file_size = os.path.getsize(project_path)

    slop = f"\n{project_name},{file_size},{project_version},{project_description},{project_developer}\n"

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        print_message(f"Connected to server at {(server_host, server_port)}", "INTERNET")

        client_socket.send("UPDATE".encode('utf-8'))

        # Send the file name we want to update
        client_socket.sendall(remote_file.encode('utf-8'))

        # Send the slop data
        client_socket.sendall(slop.encode('utf-8'))

        print_message(f"Sent update data for '{remote_file}'.", "INTERNET")

    except Exception as e:
        print_message(f"Error updating file '{remote_file}': {e}", "INTERNET")
    finally:
        client_socket.close()
        print_message("Connection closed.", "INTERNET")


"""
from client_module import download_file

# Download 'test/apps.csv' from the server and save it as 'apps.csv'
download_file('127.0.0.1', 5555, 'test/apps.csv', 'apps.csv')
"""