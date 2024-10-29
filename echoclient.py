import socket

port = int(input("port num:"))
BUFSIZE = 1024
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('192.168.31.20',port))
while True:
    msg = input("Send meg:")
    c.send(msg.encode())
    rec_msg = c.recv(BUFSIZE).decode()
    print(rec_msg)