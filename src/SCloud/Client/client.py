import socket
import tqdm
import os

from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

import time

path = os.getcwd()

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
  
def zipFile(password):
    # path to folder which needs to be zipped
    directory = 'apps'

  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile(f'apps{password}.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')

def unzipFile(password):
    with ZipFile(f'apps{password}', 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
    
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

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

def client():
    while True:
        task1 = input(str("Server: ") + ">> ")
        task = task1.split()
        if task1 == 'zip':
            try:
                password = input("Password: ")
                zipFile(password)
            except:
                pass
        if task1 == 'unzip':
            try:
                password = input("Password: ")
                unzipFile(password)
            except:
                pass
        if task1 == "exit" or task1 == "quit":
            s.close()
            exit()
        if task1 == 'upload':
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
        if len(task) > 1:
            if task[0] == "cmd":
                try:
                    s.send(bytes("cmd" , "utf-8"))
                    task = task1.split('cmd')
                    task[1] = task[1].lstrip(' ')
                    s.send(bytes(str(task[1]) , "utf-8"))
                    s.close()
                    time.sleep(0.5)
                    socket_connect()
                except:
                    pass
            if task[0] == "download":
                try:
                    s.send(bytes("download" , "utf-8"))
                    task[1] = task[1].lstrip(' ')
                    s.send(bytes(str(task[1]) , "utf-8"))
                    data = s.recv(4096).decode()
                    filename , size = data.split(SPACE)
                    filename = os.path.basename(filename)
                    file = open(str(filename),'wb')
                    terminated = False
                    upload_bar = tqdm.tqdm(range(int(size)) , f"Receiving {filename}" , unit="B", unit_scale=True, unit_divisor=1024)
                    while not terminated:
                        data = s.recv(4096)
                        if not data:
                            time.sleep(0.1)
                            socket_connect()
                            terminated = True
                            break
                        file.write(data)
                        upload_bar.update(len(data))
                    file.close()
                    
                except:
                    pass

def clientRun():
    socket_connect()
    print("You have successfully connected to the SCloud!\nTo download files, type 'download [yourfilename].ext'")
    print("Eg: download test.zip.")
    print("\nTo zip files, type 'zip' or 'unzip' to unzip a file.\nType 'upload' to upload a file.")
    print("\n\nIMPORTANT: type 'exit' or 'quit' to leave")

    client()