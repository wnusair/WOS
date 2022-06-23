import os

from cryptography.fernet import Fernet

# Define "f"
with open('cryp/mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

# Encrypt file
def encryptFile():
    file_name = input("File name to encrypt: ")

    f = Fernet(key)

    with open(file_name, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Decrypt file
def decryptFile():
    file_name = input("What is the name of the file: ")

    f = Fernet(key)

    with open(file_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(file_name, 'wb') as decrypted_files:
        decrypted_files.write(decrypted)

# Delete file
def deleteFile():
    file_name = input("What file would you like to delete: ")

    os.remove(file_name)



# crypHome page
def crypHome():
    os.system("cls")
    print("""
---------------------
1.   Encrypt File   |
---------------------
2.   Decrypt File   |
---------------------
3.   Delete File    |
---------------------
4.      Exit        |
---------------------

Copyright: Wissam Nusair 2022
MIT
""")

    c = input("Type [1 or 2 or 3 or 4]: ")

    if c == "1":
        encryptFile()
        crypHome()
    elif c == "2":
        decryptFile()
        crypHome()
    elif c == "3":
        deleteFile()
        crypHome()
    elif c == "4":
        exit()

if __name__ == "__main__":
    os.system('cls')
    crypHome()
