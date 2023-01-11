import socket
import os
import tqdm
import subprocess

path = os.getcwd()

SPACE = "<THIS_TEXT_JUST_DISTINGUISH_TEXTS>"

def serverRun():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip = input("What is your IP: ")
    port = input("What is your PORT (9999): ")


    if ip == "":
        ipName = socket.gethostname()
        ip = socket.gethostbyname(ipName)

    if port == "":
        port = "9999"


    s.bind((ip,int(port)))
    s.listen()

    for count, filename in enumerate(os.listdir()):
            os.rename(filename , filename.replace(" ","_"))
    while True:
        print("Server waiting....")
        c , _ = s.accept()
        msg = c.recv(1024)
        if(str(msg.decode("utf-8")) == "upload"):
            try:
                data = c.recv(4096).decode()
                filename , size = data.split(SPACE)
                filename = os.path.basename(filename) 
                file = open(str(filename) , 'wb')
                terminated = False
                upload_bar = tqdm.tqdm(range(int(size)) , f"Receiving {filename}" , unit="B", unit_scale=True, unit_divisor=1024)
                while not terminated:
                    data = c.recv(4096)
                    if not data:
                        terminated = True
                        break
                    file.write(data)
                    upload_bar.update(len(data))
                c.send(bytes('Received', "utf-8"))
                file.close()
            except:
                pass
        if(str(msg.decode("utf-8")) == "command"):
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
                upload_bar = tqdm.tqdm(range(int(size)) , f"Sending {filename}" , unit="B", unit_scale=True, unit_divisor=1024) 
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
