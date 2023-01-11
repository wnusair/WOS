import os
import sys

from login import *
from SCloud.Client.client import *
from apps.apps import run

def home():
    os.system('clear')
    os.system('cls')

    my_os = sys.platform
    print("OS in my system : ", my_os)


    print("""

              __          ______   _____                 
              \ \        / / __ \ / ____|                
               \ \  /\  / / |  | | (___                  
 __          ___\ \/  \/ /| |  | |\___ \    ____   _____ 
 \ \        / (_)\  /\  / | |__| |____) |  / __ \ / ____|
  \ \  /\  / / _ _\/ _\/  _\____/|_____/  | |  | | (___  
   \ \/  \/ / | / __/ __|/ _` | '_ ` _ \  | |  | |\___ \ 
    \  /\  /  | \__ \__ \ (_| | | | | | | | |__| |____) |
     \/  \/   |_|___/___/\__,_|_| |_| |_|  \____/|_____/ 

                 ---------------------------
                |          Files            |
                 ---------------------------
                |       Applications        |
                 ---------------------------

Currently using V1.6.0_ALPHA
Type 'update' to check for updates (NOT FUNCTIONAL YET)
    """)

    mainScreen = input("> ")

    if mainScreen == "files" or mainScreen == "1":
        files()

    elif mainScreen == "applications" or mainScreen == "apps" or mainScreen == "2":
        run()
    
    elif mainScreen == "update":
        os.system('clear')
        os.system('cls')

        print('\n' * 4)
        print("Type 'download update.zip' once you are connected.")

        clientRun()


        

# File Explorer
def files():
    os.system('clear')
    os.system('cls')
    list_files("./files/")

    print("Press '1' to open a file.\nPress '2' to edit or create a file.\nPress '3' to exit.")
    fileSelect = input(">> ")

    # Read/Open a file
    if fileSelect == "1":
        os.system("cls")

        list_files("./files")

        fileSelect = input(">>> ")
        fileOpen = open(fileSelect)

        print("### DOCUMENT START ###\n")
        print(fileOpen.read() + "\n")
        print("### DOCUMENT END ###\n")

        input("Press Enter to continue")
        files()
    
    # Edit or Create a file
    elif fileSelect == "2":
        os.system('clear')
        os.system('cls')

        fileSelect = input("'edit' or 'new' file: ")

        # Edit/Make a file
        if fileSelect == "new" or fileSelect == "edit":
            os.system('clear')
            os.system('cls')

            file_path = input("Type file name: ")

            with open("./apps/files/" + file_path, 'a') as file:
                print("Press enter for a new line.\nType 'exit' to exit.")
                while True:
                    line = input("")
                    if line.strip() == "exit":
                        break
                    file.write(line + "\n")

            with open("./apps/files/" + file_path, 'r') as file:
                data = file.read()

            new_data = data[:-4]

            with open("./apps/files/" + file_path, 'w') as file:
                file.write(new_data)

            input("Press Enter to continue")
            
            home()

    # Exit File Explorer
    elif fileSelect == "3":
        home()

# Makes file tree
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def terminal():
    print("""
WOS Terminal Commands:
type any CMD command
""")
    
    run = True
    while run:
        directory = os.getcwd()

        cmd = input(f"""
user-root#
│
└── {directory} $""")

        if cmd == "exit" or cmd == "quit":
            home()
        else:
            os.system(cmd)
