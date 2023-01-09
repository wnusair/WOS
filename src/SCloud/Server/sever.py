import socket
import os
import tqdm

from login import *

path = os.getcwd()

SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

s = socket.socket()

ip = input("What is your IP: ")
port = input("What PORT would you like to connect to (default = 9999): ")

if ip == "":
    ipName = socket.gethostname()
    ip = socket.gethostbyname(ipName)

if port == "":
    port = "9999"

s.bind((ip, int(port)))
s.listen(1)

for count, filename in enumerate(os.listdir()):
        os.rename(filename , filename.replace(" ","_"))

def serverRun():
    print("[SERVER IS AWAKE]")

    while True:
        print("[SERVER] waiting....")
        c , _ = s.accept()
        msg = c.recv(1024)
        if(str(msg.decode("utf-8")) == "backup"):
            received = c.recv(4096).decode()
            filename, filesize = received.split(SPACE)
            # remove absolute path if there is
            filename = os.path.basename(filename)
            # convert to integer
            filesize = int(filesize)
            # start receiving the file from the socket
            # and writing to the file stream
            progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "wb") as f:
                while True:
                    # read 1024 bytes from the socket (receive)
                    bytes_read = c.recv(4096)
                    if not bytes_read:    
                        # nothing is received
                        # file transmitting is done
                        break
                    # write to the file the bytes we just received
                    f.write(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))

            # close the client socket
            c.close()
            # close the server socket
            s.close()

        if(str(msg.decode("utf-8")) == "upload"):
            try:
                data = c.recv(4096).decode()
                filename , size = data.split(SPACE)
                filename = os.path.basename(filename) 
                file = open(str(filename) , 'wb')
                terminated = False
                upload_bar = tqdm.tqdm(range(int(size)) , f"[SERVER] Receiving {filename}" , unit="B", unit_scale=True, unit_divisor=1024)
                while not terminated:
                    data = c.recv(4096)
                    if not data:
                        terminated = True
                        break
                    file.write(data)
                    upload_bar.update(len(data))
                file.close()
            except:
                pass
        if(str(msg.decode("utf-8")) == "ls"):
            try:
                data = os.system("tree")
                c.send(bytes(data , "utf-8"))
            except:
                pass
        if(str(msg.decode("utf-8")) == "cmd"):
                try:
                    data = str(c.recv(4096).decode("utf-8"))
                    os.system(data)

                    c.send(bytes(data, "utf-8"))
                except:
                    pass
        if(str(msg.decode("utf-8")) == "download"):
            try:
                data = str(c.recv(4096).decode("utf-8"))
                filename = str(data)
                size = os.path.getsize(data)
                c.send(f"{filename}{SPACE}{size}".encode())
                upload_bar = tqdm.tqdm(range(int(size)) , f"[SERVER] Sending {filename}" , unit="B", unit_scale=True, unit_divisor=1024) 
                filename = filename.replace(" ","")
                file = open(filename , "rb")
                terminated = False
                while not terminated:
                    data = file.read(4096)
                    if not data:
                        c.close()
                        terminated = False
                    c.sendall(data)
                    upload_bar.update(len(data))
                file.close()
                
            except:
                pass
