import socket

port = 2500
BUFSIZE = 1024
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = input("Send meg:")
c.sendto(msg.encode(), ('localhost', port))
rec_msg, addr = c.recvfrom(BUFSIZE)
print(rec_msg.decode())
