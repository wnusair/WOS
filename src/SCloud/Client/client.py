import socket
import tqdm
import os
import time

from tkinter import *
import tkinter as tk
from tkinter import filedialog

from zipfile import ZipFile

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
  
def zipFile():
    # path to folder which needs to be zipped
    directory = 'apps'

  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile('apps.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')


def clientRun():

    global s, ip, port

    s = socket.socket()

    ip = input("What IP would you like to connect to: ")
    port = input("What PORT would you like to connect to (default = 9999): ")


    s.connect((ip, int(port)))

    SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

    print("[SERVER] You have connected the SCloud\nUse command upload to upload files in cloud.\nUser command download <filename.ext> to download files")
    print("Use cmd commands by cmd <command> Eg: cmd mkdir Documents")

    while True:
        task1 = input(str("> "))
        task = task1.split()
        if task1 == "exit" or task1 == "quit":
            exit()
        
        if task1 == "backup":
            zipFile()
            # start sending the file
            size = os.path.getsize('./apps.zip')

            s.send(f"{'./apps.zip'}{SPACE}{size}".encode())
            progress = tqdm.tqdm(range(int(size)), f"Sending {'./apps.zip'}", unit="B", unit_scale=True, unit_divisor=1024)
            with open('./apps.zip', "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(4096)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    s.sendall(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))
            # close the socket
            s.close()
            clientRun()

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
                        terminated = True
                    s.sendall(data)
                    upload_bar.update(len(data))
                file.close()
                clientRun()
            except:
                pass
                clientRun()
        if len(task) > 1:
            if task[0] == "cmd":
                try:
                    s.send(bytes("cmd" , "utf-8"))
                    task = task1.split('cmd')
                    task[1] = task[1].lstrip(' ')
                    s.send(bytes(str(task[1]) , "utf-8"))
                    s.close()
                    time.sleep(0.5)
                    clientRun()
                except:
                    pass
                    clientRun()
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
                            terminated = True
                            break
                        file.write(data)
                        upload_bar.update(len(data))
                    file.close()
                    clientRun()
                except:
                    pass
                    clientRun()