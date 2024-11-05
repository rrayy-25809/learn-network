import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',2500))
s.listen(1)
print('Waiting...')

cilent, addr = s.accept()
print(f'Client{addr} say {cilent.recv(1024).decode()}')
filepath = input("input filename")
filename = filepath.split('/')[-1]

cilent.sendall(filename.encode())
with open(filepath, 'rb') as f:
    cilent.sendfile(f,0)
print('Sending Complite')
s.close()