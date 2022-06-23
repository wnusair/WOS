import os
from time import sleep

from crypHome import *
from cryptography.fernet import Fernet

# Define "f"
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

# crypLogin
def crypLogin():
    passwordInput = input("Password: ")
    with open('erp.txt', 'rb') as rawPassword:
        encrypted = rawPassword.read()

    decrypted = f.decrypt(encrypted)

    with open('dp.txt', 'wb') as decryptedPassword:
        decryptedPassword.write(decrypted)

    with open("dp.txt", "rb") as copyPassword:
        password = copyPassword.readlines()

    openPassword = open("dp.txt")

    password = openPassword.read()

    openPassword.close()

    if passwordInput == password:
        os.remove('dp.txt')
        print("Logged in")
        sleep(1)
        home()
    else:
        os.remove('dp.txt')
        quit()
"""

Could have been 😭

# Register
def register():
    username = input("What would you like your username to be: ")
    with open("users.txt", "a") as usernames:
        usernames.write(username + "\n")
"""

# crypLogin or Register?
if __name__ == "__main__":
    os.system('cls')
    crypLogin()
