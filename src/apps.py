import socket
import os
import screens

from wissampy import print_message, create_db, register_user, login_user

def app_screen() -> None:
    app_screen = screens.Screen(
        "APP SCREEN",
        ["1. Upload", "2. Download", "3. Delete", "4. Quit"])
    choice = app_screen.display()
    
    if choice == "1":
        upload()
    elif choice == "2":
        download()
    elif choice == "3":
        delete()
    elif choice == "4":
        exit()
    else:
        print_message("Invalid choice.", "red")

def download() -> None:
    pass

def upload() -> None:
    pass

def delete() -> None:
    pass


if __name__ == "__main__":
    app_screen()