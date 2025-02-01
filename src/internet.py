import socket
import os
import screens

from wissampy import print_message, create_db, register_user, login_user

def internet_screen() -> None:
    internet_screen = screens.Screen(
        "INTERNET SCREEN",
        ["1. Connect", "2. Host", "3. Quit"])
    choice = internet_screen.display()
    
    if choice == "1":
        connect()
    elif choice == "2":
        host()
    elif choice == "3":
        exit()
    else:
        print_message("Invalid choice.", "red")

def connect() -> None:
    HOST = input("Enter host IP: ")
    PORT = int(input("Enter host port: "))

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print_message("Connected to host.", "SUCCESS")
    except Exception as e:
        print_message(str(e), "INTERNET")

def host() -> None:
    PORT = int(input("Enter port to host on: "))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", PORT))
            s.listen()
            print_message(f"Hosting on port {PORT}. Waiting for connections...", "SUCCESS")
            conn, addr = s.accept()
            with conn:
                print_message(f"Connected by {addr}", "SUCCESS")
    except Exception as e:
        print_message(str(e), "INTERNET")


if __name__ == "__main__":
    internet_screen()