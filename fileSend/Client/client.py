import socket
import tqdm
import os
from tkinter import *
from tkinter import filedialog
import time

path = os.getcwd()

def socket_connect():
    global s
    ip = "192.168.1.111"
    port = 9999
    s = socket.socket()
    s.connect((ip,port))

def clientRun():
    socket_connect()

    SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

    print("*You are successfully connected with the server* Use command upload to upload files in cloud . Use command ls to list files in server . User command download <filename.ext> to download files")
    print("Use cmd commands by cmd <command> Eg: cmd mkdir Documents")

    while True:
        task1 = input(str("Server: ") + ">> ")
        task = task1.split()
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
        if task1 == 'ls':
            try:
                s.send(bytes("ls" , "utf-8"))
                data = s.recv(4096)
                s.close()
                time.sleep(0.5)
                socket_connect()
                print(str(data.decode('utf-8')))
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
