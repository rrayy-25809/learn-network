import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',2500))
sock.listen(1)
print('Waiting..')
dict = {1:'one',2:'two',3:'three',4:'four',5:'five'}
conn, (remotehost, remoteport) = sock.accept()
print(f'Client Connected {remotehost}:{remoteport}')
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(data)
    try:
        conn.send(dict[int(data)].encode())
    except:
        conn.send(data.encode())
sock.close()