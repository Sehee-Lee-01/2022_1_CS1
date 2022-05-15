import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))

s.listen(1)
print('Socket Listen Start!')

connector, addr = s.accept()
while True:
        data = connector.recv(1024)
        if not data: break
        print('Message from Client: ' + data.decode('utf-8'))
        response = data.decode('utf-8')[-1::-1]
        connector.send(response.encode('utf-8'))
s.close()
