import os
import sys

from cryp.crypHome import crypHome
from login import *

from SCloud.Client.client import clientRun
from SCloud.Server.sever import serverRun

import os

def run():
    os.system('clear')
    os.system('cls')

    apps = "SCloud Server\nSCloud Client\nCPP (File Encryption)\nTerminal\n\nNEW!\nInstalled"
    print(apps)

    appOpen = input("> ")
    if appOpen == "SCloud Server" or appOpen == "scloud server" or appOpen == "server" or appOpen == "1":
        os.system('clear')
        os.system('cls')

        print("WARNING: You must restart the program after running the server.")
        serverRun()
    elif appOpen == "SCloud Client" or appOpen == "scloud client" or appOpen == "client" or appOpen == "2":
        os.system('clear')
        os.system('cls')
        
        print("WARNING: You must restart the program after running the client.")
        clientRun()

    elif appOpen == "cpp" or appOpen == "CPP" or appOpen == "3":
        os.system('clear')
        os.system('cls')

        crypHome()

    elif appOpen == "terminal" or appOpen == "cmd":
        os.system('clear')
        os.system('cls')

        terminal()
    
    elif appOpen == "installed" or appOpen == "Installed":
        os.system('clear')
        os.system('cls')

        installed()


# Installed Apps
def installed():
    files = []

    print(os.listdir('./apps'))

    folder = input("What folder is your app in (type 'quit' or 'exit' to leave): ")
    if folder == "quit" or folder == "exit":
        run()

    file = input("Example: myapp.exe\nWhat is the file name (must be .exe file):")

    os.chdir("apps/" + folder)
    os.system("start " + file)

    run()


# Terminal
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
