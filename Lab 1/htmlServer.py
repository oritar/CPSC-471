#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', 8000))
serverSocket.listen()

while True:
    #Establish the connection

    print('\nReady to serve...')

    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print(message.decode('utf-8'))
    
    try:
        filename = message.split()[1] 
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send(str.encode('\nFrom Server: HTTP/1.1 200 OK', 'utf-8'))
        connectionSocket.send(str.encode('\nConnection: close', 'utf-8'))
        connectionSocket.send(str.encode('\nContent-Length: ' + str(sys.getsizeof(outputdata)), 'utf-8'))
        connectionSocket.send(str.encode('\nContent-Type: text/html\n', 'utf-8'))
        connectionSocket.send(str.encode('\n'))
        connectionSocket.sendall(str.encode("" + outputdata + "", 'utf-8'))
        outputdata = f.read(1024)

        f.close()
        connectionSocket.close()

    except IOError:
        f = open('404.html')
        outputdata = f.read()
        connectionSocket.sendall(str.encode('\nInvalid URL.', 'utf-8'))
        connectionSocket.sendall(str.encode('\nHTTP/1.1 404 Not Found\n\n', 'utf-8'))
        connectionSocket.sendall(str.encode("" + outputdata + "", 'utf-8'))
        connectionSocket.close()

    serverSocket.close()

    sys.exit() #Terminate the program after sending the corresponding data