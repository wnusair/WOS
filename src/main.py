import wissampy
import auth
import screens

from terminal import terminal_screen

def main():
    wissampy.clear_screen()
    auth.auth()

    main_screen = screens.Screen(
        "MAIN SCREEN",
        ["1. Terminal", "2. Apps", "3. Quit"])
    choice = main_screen.display()

    if choice == "1":
        terminal_screen()
    elif choice == "2":
        pass
    elif choice == "3":
        exit()
    else:
        wissampy.cprint("Invalid choice.", "red")

if __name__ == "__main__":
    wissampy.first_install()
    main()