import os
import sys

from cryp.crypHome import crypHome

from fileSend.Client.client import clientRun
from fileSend.Server.sever import serverRun


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
    """)

    mainScreen = input("> ")

    if mainScreen == "files" or mainScreen == "1":
        files()
    elif mainScreen == "applications" or mainScreen == "apps" or mainScreen == "2":
        applications()

# File Explorer
def files():
    os.system('clear')
    os.system('cls')
    list_files(".")

    print("Press '1' to open a file.\nPress '2' to edit or create a file.\nPress '3' to exit.")
    fileSelect = input(">> ")

    # Read/Open a file
    if fileSelect == "1":
        os.system("cls")

        list_files(".")

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

        # Edit a file
        if fileSelect == "edit":
            list_files(".")

            fileSelect = input(">>> ")
            fileOpen = open(fileSelect)

            os.system('clear')
            os.system('cls')
            print("### DOCUMENT START ###\n")
            print(fileOpen.read() + "\n")
            print("### DOCUMENT END ###\n\n")

            print("Press enter for a new line.\nType 'exit' to exit.")

            exit = False

            while exit == False:
                with open(fileSelect, "a") as file:
                    fileEdit = input("")
                    if fileEdit == "exit":
                        exit = True

                    file.write(fileEdit + "\n")
            
            input("Press Enter to continue")
            files()
        
        # Make new file
        elif fileSelect == "new":
            os.system('clear')
            os.system('cls')

            print("Type file name.")
            fileSelect = input(">>> ")

            os.system('clear')
            os.system('cls')
            print("Press enter for a new line.\nType 'exit' to exit.")

            exit = False

            while exit == False:
                with open(fileSelect, "a") as file:
                    fileEdit = input("")
                    if fileEdit == "exit":
                        exit = True

                    file.write(fileEdit + "\n")
            
            input("Press Enter to continue")
            files()

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

def applications():
    os.system('clear')
    os.system('cls')

    apps = "fileSendServer\nfileSendClient\nCPP (File Encryption)\n"
    print(apps)

    appOpen = input("> ")
    if appOpen == "fileSendServer":
        os.system('clear')
        os.system('cls')

        print("WARNING: You must restart the program after running the server.")
        serverRun()
    elif appOpen == "fileSendClient":
        os.system('clear')
        os.system('cls')
        
        print("WARNING: You must restart the program after running the client.")
        clientRun()
    elif appOpen == "cpp":
        os.system('clear')
        os.system('cls')

        crypHome()