import socket,time,sys

###Init

s=socket.socket()
host=socket.gethostname()
print("Server will start on host:",host)
port=8080

s.bind((host,port))

print("Server done binding to the host and the port successfully")
print("")
print("SERVER ID READY /n")
s.listen(1)  #no of connection
conn,addr=s.accept()
print(addr,"Has connected to the server and is online")
print("")
while True:
    msg=input(str(">>"))
    msg=msg.encode()
    conn.send(msg)
    imsg=conn.recv(1024)
    imsg=imsg.decode()
    print("Clint:",imsg)






