import socket,time,sys

###Init

s=socket.socket()
host=input(str("Enter the host name="))
port=8080
s.connect((host,port))
print("Connected to chat server")
while True:
    imsg=s.recv(1024)
    imsg=imsg.decode()
    print("Server:",imsg)
    msg=input(str(">>"))
    msg=msg.encode()
    s.send(msg)
