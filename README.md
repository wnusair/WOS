# WOS (Wissam OS)

This is the official Wissam OS, a versatile operating system that works on Windows, Linux, and Mac. It is designed to be open and extensible, allowing anyone to create their own "app" using the provided `wissampy.py` and `screens.py` files.

## Table of Contents
- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Creating Your Own App](#creating-your-own-app)
- [Function Documentation](#function-documentation)
  - [wissampy.py](#wissampy.py)
  - [screens.py](#screens.py)
- [Coming Soon](#coming-soon)
- [Closing Remarks](#closing-remarks)

## Introduction
WOS is a simple and extensible operating system that allows users to create and manage applications easily. It includes basic authentication, app management, and screen management functionalities.

## How It Works
WOS uses CSV files to manage user data and app data. It provides a simple terminal-based interface for users to interact with the system. The main components of WOS are:
- `wissampy.py`: Contains utility functions and database management functions.
- `screens.py`: Contains the `Screen` class for creating and displaying screens.
- `auth.py`: Manages user authentication.
- `apps.py`: Manages the app screen and displays installed apps.
- For client-side users, you will only need the `apps` `RUN` `src` folders. The server uses `storage` to keep the uploaded files and `files` to store csv's.
## Creating Your Own App
To create your own app, you can use the functions provided in `wissampy.py` and `screens.py`. Follow these steps:
1. Create a new Python file for your app.
2. Import the necessary functions from `wissampy.py` and `screens.py`.
3. Define your app's functionality using the provided functions.
4. Add your app to the `apps.csv` file.

## Setting Up the Server
To set up the WOS server, all the folders and files are already present. Although it may look confusing, the `storage` and `files` folders are meant for the server. To start the server, you will need to simply run src/server.py and adjust the ip address in the client file and apps file to show your desired port and IP.

## Function Documentation

### wissampy.py
#### `detect_os(func: any) -> None`
Wrapper to detect the operating system and pass it to the function.

#### `print_message(message: str, message_type: str) -> None`
Prints a message with a specific 'type' and its designated color. Types include 'SYSTEM,' 'FILE,' 'SUCCESS,' and 'INTERNET.' Yes, they must be written in all CAPS.

#### `cprint(message: str, color: str) -> None`
Prints a message with a specific color.

#### `clear_screen(system: str) -> None`
Clears the terminal screen based on the detected operating system.

#### `create_db(db_name: str, default_rows: list) -> None`
Creates a CSV database with the given name.

#### `register_user(db_name: str, credentials: list) -> None`
Creates a user in the CSV database with the given name.

#### `login_user(db_name: str, credentials: list) -> None`
Checks if a user is in the database with the given name.

#### `first_install() -> None`
Creates the necessary databases for the first time.

### screens.py
#### `Screen`
Class for creating and displaying screens.

##### `__init__(self, title: str, options: list) -> None`
Initializes the screen with a title and options.

##### `display(self) -> str`
Displays the screen and returns the user's choice.

<strong>Example Use:<strong>
```
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
```

## Coming Soon
- Connecting to a central database for app updates and user management.
- Improved user interface with more customization options.
- Enhanced security features for user authentication.
- Integration with cloud storage for app data.

## Closing Remarks
WOS is an open and extensible operating system that allows anyone to create their own apps. We encourage you to explore the provided functions and create your own unique applications. If you have any questions or need assistance, feel free to reach out.

Happy coding!