import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',5000))
s.listen(5)
while True:
    client, addr =s.accept()
    print()
    print(f"connection by {addr}")
    client.send(time.ctime(time.time()).encode())
    client.close()