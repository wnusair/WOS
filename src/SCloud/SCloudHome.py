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
    TCP_IP = 'localhost'
    TCP_PORT = 9001
    BUFFER_SIZE = 1024


    class ClientThread(Thread):

        def __init__(self, ip, port, sock):
            Thread.__init__(self)
            self.ip = ip
            self.port = port
            self.sock = sock
            print(" New thread started for "+ip+":"+str(port))

        def run(self):
            filename = 'anon234.jpeg'
            f = open(filename, 'rb')
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    #print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break


    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []

    while True:
        tcpsock.listen(5)
        print("Waiting for incoming connections...")
        (conn, (ip, port)) = tcpsock.accept()
        print('Got connection from ', (ip, port))
        newthread = ClientThread(ip, port, conn)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()
