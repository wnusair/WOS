import os
import screens

from client import download_file, update_csv

from wissampy import print_message, create_db, register_user, login_user

def app_screen() -> None:
    while True:
        app_screen = screens.Screen(
            "APP SCREEN",
            ["1. App Store", "2. My Apps", "3. Upload App", "4. Exit"])
        choice = app_screen.display()
        
        if choice == "1":
            all_apps()
        elif choice == "2":
            installed_apps()
        elif choice == "3":
            update_csv('10.25.111.103', 5555, 'files/apps.csv')
        elif choice == "4":
            break
        else:
            print_message("Invalid choice.", "red")

def all_apps() -> None:
    download_file('10.25.111.103', 5555, 'files/apps.csv', 'apps.csv')
    with open("apps.csv", 'r') as file:
        for app in file:
            print(app)
    
    choice = input("Would you like to download an app? (y/n): ")

    if choice.lower() == "y":
        app_name = input("Enter the name of the app you want to download: ")
        download_file('10.25.111.103', 5555, f'storage/{app_name}.py', f'apps/{app_name}.py')
    elif choice.lower() == "n":
        return
    else:
        print("Invalid choice.")
    
    # ADD CHECKING INTERNET TO UPDATE LIST OF APPS AND ADD ABILITY TO INSTALL THEM

def installed_apps() -> None:
    apps_dir = "apps"
    apps = os.listdir(apps_dir)
    for app in apps:
        print(app)

    choice = input("Would you like to uninstall an app? (y/n): ")

    if choice.lower() == "y":
        app_name = input("Enter the name of the app you want to uninstall: ")
        os.remove(f"apps/{app_name}.py")
    elif choice.lower() == "n":
        return
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    app_screen()