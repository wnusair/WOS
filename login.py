from cryptography.fernet import Fernet
from time import sleep

from home import *

import os

with open('cryp/mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

def login():
    passwordInput = input("Password: ")
    with open('cryp/erp.txt', 'rb') as rawPassword:
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