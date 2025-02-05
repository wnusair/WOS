import socket
import os
import screens

from wissampy import print_message, create_db, register_user, login_user

def get_system_path() -> str:
    return os.path.dirname(os.path.realpath(__file__)) + " $ "

def terminal_screen() -> None:
    while True:
        command = input(get_system_path())
        try:
            if command == "exit":
                break

            os.system(command)
        except Exception as e:
            print_message(str(e), "SYSTEM")

if __name__ == "__main__":
    terminal_screen()