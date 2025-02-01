import os
import csv

# FROM IMPORTS
from termcolor import colored

# WRAPPERS
def detect_os(func: any) -> None:
    """Wrapper to detect the operating system and pass it to the function."""
    def wrapper(*args, **kwargs):
        if os.name == "nt":
            system = "Windows"
        elif os.name == "posix":
            system = "Unix"
        else:
            system = "Unknown"
        return func(system, *args, **kwargs)
    return wrapper


# print error
def print_message(message: str, message_type: str) -> None:
    """ PRINTS A MESSAGE WITH A SPECIFIC 'TYPE' AND ITS DESIGNATED COLOR """
    if message_type == "INTERNET":
        print(colored(f"[{message_type}] {message}", "yellow"))
    elif message_type == "FILE":
        print(colored(f"[{message_type}] {message}", "blue"))
    elif message_type == "SYSTEM":
        print(colored(f"[{message_type}] {message}", "red"))
    elif message_type == "SUCCESS":
        print(colored(f"[{message_type}] {message}", "green"))

def cprint(message: str, color: str) -> None:
    """ PRINTS A MESSAGE WITH A SPECIFIC COLOR """
    print(colored(message, color))

@detect_os
def clear_screen(system: str) -> None:
    """Clear the terminal screen based on the detected operating system."""
    if system == "Windows":
        os.system("cls")  # Windows uses 'cls'
    elif system == "Unix":
        os.system("clear")  # Linux/macOS use 'clear'
    else:
        print("[ERROR] Unsupported Operating System. Cannot clear screen.")



# Database
def create_db(db_name: str, default_rows: list) -> None:
    """ Creates a csv db with the given name """

    if not os.path.exists(f"{db_name}.csv"):
        with open(f"{db_name}.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(default_rows)
            print_message("Database created successfully.", "SUCCESS")
    else:
        print_message("Database already exists.", "FILE")


def register_user(db_name: str, credentials: list) -> None:
    """ Creates a user in the csv db with the given name """

    if not os.path.exists(f"{db_name}.csv"):
        print_message("Database does not exist.", "FILE")
    else:
        try:
            with open(f"{db_name}.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(credentials)
                print_message("User registered successfully.", "SUCCESS")
        except Exception as e:
            print_message(str(e), "FILE")
        finally:
            print_message("File Loop Closed", "FILE")

def login_user(db_name: str, credentials: list) -> None:
    """ chekcs if user is in db with the given name """

    if not os.path.exists(f"{db_name}.csv"):
        print_message("Database does not exist.", "FILE")
    else:
        try:
            with open(f"{db_name}.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row == credentials:
                        print_message("User logged in successfully.", "SUCCESS")
        except Exception as e:
            print_message(str(e), "FILE")
        finally:
            print_message("File Loop Closed", "FILE")









# Example Usage
if __name__ == "__main__":
    """ TEST OUT THE ALL FUNCTIONS IN THE FILE, AS WELL AS THE SYSTEM MESSAGES """
    print("sigma sigma boy?!?!?!?!")

    try:
        clear_screen()
    except Exception as e:
        print_message(str(e), "SYSTEM")
    
    print_message("Screen cleared successfully.", "SUCCESS")
