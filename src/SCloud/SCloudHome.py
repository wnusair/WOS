import socket
import tqdm
import os

from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

import time

path = os.getcwd()

def SCloudHome():
    socket_connect()

    print("""
Welcome to the SCloud! Here is a list of commands you can run (ONLY AS CLIENT):
 - Upload: This uploads a file to the SCloud Server
 - Download [filename]: This downloads a file from the SCloud Server
 - zip: This backs up your 'apps' folder to the SCloud Server
 - unzip: This unzips the folder you downloaded from the SCloud
 - update: Coming Soon!

""")
    choice = input(">> ")

    if choice == "upload":
        upload()

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths        

def socket_connect():
    global s
    ip = input("What is your IP: ")
    port = input("What is your PORT (9999): ")

    if ip == "":
        ipName = socket.gethostname()
        ip = socket.gethostbyname(ipName)
    
    if port == "":
        port = "9999"

    s = socket.socket()
    s.connect((ip, int(port)))

SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

def upload():
    try:
        data = filedialog.askopenfile(initialdir="/")
        filename = str(data.name)
        size = os.path.getsize(filename)
        s.send(bytes("upload" , "utf-8"))
        s.send(f"{filename}{SPACE}{size}".encode())
        upload_bar = tqdm.tqdm(range(int(size)) , f"Sending {filename}" , unit="B", unit_scale=True, unit_divisor=1024) 
        file = open(filename , "rb")
        terminated = False
        while not terminated:
            data = file.read(4096)
            if not data:
                s.close()
                time.sleep(0.5)
                socket_connect()
                terminated = True
            s.sendall(data)
            upload_bar.update(len(data))
        file.close()
    except:
        pass