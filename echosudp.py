import socket

PORT = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',PORT))

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    print(f"Received message by {addr}: {data.decode()}")
    sock.sendto(data,addr)