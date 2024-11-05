import socket

BUFFSIZE = 1024
PORT = 2500

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('localhost', PORT)

while True:
    msg = input('<- ')
    sock.sendto(msg.encode(),addr)
    print("->", end='')
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())