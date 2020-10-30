from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))

message = 'GET ' + '/' + sys.argv[3] + ' HTTP/1.1'

clientSocket.send(message.encode())
clientSocket.sendall(str.encode('\nHost: ' + HOST + ':' + str(PORT), 'utf-8'))
clientSocket.send(str.encode('\nConnection: close\n', 'utf-8'))

while True:
    data = clientSocket.recv(1024)

    if len(data) <= 0:
        break

    print(data.decode('utf-8'))

clientSocket.close()
sys.exit()