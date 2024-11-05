import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.31.20',2500))
s.send('I am ready!'.encode())

filename = s.recv(1024).decode()
with open(f"recv/{filename}",'wb') as f:
    while True:
        data = s.recv(8192)
        if not data:
            break
        f.write(data)

print('I get file!')
s.close()