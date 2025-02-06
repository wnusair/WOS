import os
import screens

from client import download_file, update_csv

from wissampy import print_message, create_db, register_user, login_user

def app_screen() -> None:
    while True:
        app_screen = screens.Screen(
            "APP SCREEN",
            ["1. All Apps", "2. Installed Apps", "3. Add App", "4. Exit"])
        choice = app_screen.display()
        
        if choice == "1":
            all_apps()
        elif choice == "2":
            installed_apps()
        elif choice == "3":
            update_csv('127.0.0.1', 5555, 'files/apps.csv')
        elif choice == "4":
            break
        else:
            print_message("Invalid choice.", "red")

def all_apps() -> None:
    download_file('127.0.0.1', 5555, 'files/apps.csv', 'apps.csv')
    with open("apps.csv", 'r') as file:
        for app in file:
            print(app)
    
    # ADD CHECKING INTERNET TO UPDATE LIST OF APPS AND ADD ABILITY TO INSTALL THEM

def installed_apps() -> None:
    apps_dir = "apps"
    apps = os.listdir(apps_dir)
    for app in apps:
        print(app)

if __name__ == "__main__":
    app_screen()