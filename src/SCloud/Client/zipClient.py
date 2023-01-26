import socket

soc = socket.socket()
soc.connect(('localhost',8080))
savefilename = input("enter file name to receive: ")
with soc,open(savefilename,'wb') as file:
    while True:
        recvfile = soc.recv(4096)
        if not recvfile: break
        file.write(recvfile)
print("File has been received.")