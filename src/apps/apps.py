import os

def run():
    while True:
        print("What project would you like to run?\nex: app.exe")
        
        app = input("> ")

        os.system("start " + app)