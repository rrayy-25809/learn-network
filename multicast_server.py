from socket import *
import struct

MAX_BUFF = 1024
group_aaddr = ("224.0.0.255",5005)
r_sock = socket(AF_INET, SOCK_DGRAM)
r_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r_sock.bind(('',5005))

while True:
    rmsg, addr = r_sock.recvfrom(MAX_BUFF)
    print(f"Received {rmsg.decode()} from {addr}")
    r_sock.sendto('ACK'.encode(),addr)