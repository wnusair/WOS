import socket
import sys
import os
import time

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

def upload_file(server_host, server_port, local_file, remote_file):
    """
    Connect to the specified server, send `local_file`,
    and save it on the server as `remote_file`.

    Usage example:
        from client_module import upload_file
        upload_file('', 5555, 'apps.csv', 'test/apps.csv')
    """

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print_message(f"Connected to server at {(server_host, server_port)}", "INTERNET")

        client_socket.send("UPLOAD".encode('utf-8'))

        # Send the file name we want
        time.sleep(1)
        client_socket.sendall(remote_file.encode('utf-8'))

        # Send the file data
        with open(local_file, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client_socket.sendall(data)

        print_message(f"Uploaded '{local_file}' to '{remote_file}'.", "INTERNET")

    except Exception as e:
        print_message(f"Error uploading file '{local_file}': {e}", "INTERNET")
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
        time.sleep(1)

        client_socket.connect((server_host, server_port))
        print_message(f"Connected to server at {(server_host, server_port)}", "INTERNET")

        time.sleep(1)
        client_socket.send("UPDATE".encode('utf-8'))

        """
        NOTE, THIS DOESNT ACTUALLY SEND THE FILE DATA, JUST ITS INFORMATION
        """

        # Send the slop data
        time.sleep(1)
        client_socket.sendall(slop.encode('utf-8'))

        print_message(f"Sent update data for '{remote_file}'.", "INTERNET")

        time.sleep(1)

        # Send the file data
        upload_file(server_host, server_port, project_path, remote_file)

    except Exception as e:
        print_message(f"Error updating file '{remote_file}': {e}", "INTERNET")
    finally:
        download_file('127.0.0.1', 5555, 'files/apps.csv', 'apps.csv')

        client_socket.close()
        print_message("Connection closed.", "INTERNET")


"""
from client_module import download_file

# Download 'test/apps.csv' from the server and save it as 'apps.csv'
download_file('127.0.0.1', 5555, 'test/apps.csv', 'apps.csv')
"""