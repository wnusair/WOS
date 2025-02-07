import wissampy
import auth
import screens

from terminal import terminal_screen
from apps import app_screen
def main():
    wissampy.clear_screen()
    auth.auth()

    while True:
        main_screen = screens.Screen(
            "MAIN SCREEN",
            ["1. Terminal", "2. Apps", "3. Quit"])
        choice = main_screen.display()

        if choice == "1":
            terminal_screen()
        elif choice == "2":
            app_screen()
        elif choice == "3":
            break
        else:
            wissampy.cprint("Invalid choice.", "red")

if __name__ == "__main__":
    wissampy.first_install()
    main()