import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',5000))
print("현재시각",c.recv(1024).decode())