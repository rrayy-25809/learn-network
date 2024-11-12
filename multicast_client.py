from socket import *
import struct

group_aaddr = ("224.0.0.255",5005)
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.settimeout(0.5)

TTL = struct.pack('@i', 2)
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)

while True:
    rmsg = input('ur msg')
    s_sock.sendto(rmsg.encode(), group_aaddr)
    while True:
        try:
            response, addr = s_sock.recvfrom(1024)
        except timeout:
            break
        else:
            print(f"{response.decode()} from {addr}")