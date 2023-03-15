import socket
import tqdm
import os

from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

from threading import Thread

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
    ip = input("What IP would you like to connect to: ")
    port = input("What PORT would you like to connect to (9999): ")

    if ip == "":
        ipName = socket.gethostname()
        print(str(ipname))
        ip = socket.gethostbyname(ipName)
    
    if port == "":
        port = "9999"

    s = socket.socket()
    s.connect((ip, int(port)))

SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

def upload():
    TCP_IP = input("IP you would like to connect to: ")
    TCP_PORT = 9999
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    recived_f = 'imgt_thread'+str(time.time()).split('.')[0]+'.jpeg'
    with open(recived_f, 'wb') as f:
        print('file opened')
        while True:
            #print('receiving data...')
            data = s.recv(BUFFER_SIZE)
            print('data=%s', (data))
            if not data:
                f.close()
                print('file close()')
                break
            # write data to a file
            f.write(data)

    print('Successfully get the file')
    s.close()
    print('connection closed')
