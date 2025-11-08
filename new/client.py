import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))
s.send("Hello server!".encode())

with open('received_file', 'wb') as f:
    print('Receiving data...')
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

print('Successfully received the file')
s.close()
print('Connection closed')
