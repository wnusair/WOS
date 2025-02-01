from wissampy import cprint, clear_screen, register_user, login_user, create_db

def main() -> str:
    create_db("users", ["username", "password"])
    cprint("AUTHENTICATION SCREEN", "green")
    cprint("1. Login", "blue")
    cprint("2. Register", "blue")
    cprint("3. Exit", "blue")

    choice = input("Enter your choice: ")

    return choice


def auth() -> None:
    choice = main()

    while True:
        if choice == "1":
            login()
            break
        elif choice == "2":
            register()
            break
        elif choice == "3":
            exit()
        else:
            cprint("Invalid choice.", "red")

def login() -> None:
    username = input("Username: ")
    password = input("Password: ")

    login_user("users", [username, password])

def register() -> None:
    username = input("Username: ")
    password = input("Password: ")

    register_user("users", [username, password])

if __name__ == "__main__":
    auth()
            


