import socket

BUFSIZE = 1024
ip_con = input("IP:Port(default: localhost:2500)")
try:
    con = tuple(ip_con.split(":"))
except:
    con = ('localhost', '2500')
c = socket.create_connection(con)
msg = input("Send meg:")
c.sendall(msg.encode())
rec_msg = c.recv(BUFSIZE).decode()
print(rec_msg)
c.close()