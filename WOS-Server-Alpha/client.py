import socket

import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# Now you can import wissampy
from wissampy import print_message

HOST = "localhost"  # Server IP address
PORT = 55000        # Server port
BUFFER_SIZE = 1024  # Size of the message buffer

def start_client():
    """Connects to the server and sends messages."""
    try:
        # Create a socket for the client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        client.connect((HOST, PORT))
        print_message(f"Connected to server at {HOST}:{PORT}", "INTERNET")

        # Loop to send messages
        while True:
            # Get message input from the user
            message = input("Enter message to send (or 'exit' to quit): ")
            
            if message.lower() == 'exit':  # Exit the loop if the user types 'exit'
                print_message("Closing connection...", "INTERNET")
                break
            
            # Send the message to the server
            client.sendall(message.encode('utf-8'))

            # Receive the server's response
            response = client.recv(BUFFER_SIZE).decode('utf-8')
            print_message(f"Server response: {response}", "INTERNET")

    except ConnectionRefusedError:
        print_message("Error: Unable to connect to the server. Is it running?", "INTERNET")
    except Exception as e:
        print_message(f"An error occurred: {e}", "INTERNET")
    finally:
        # Close the client socket
        client.close()

if __name__ == "__main__":
    start_client()
