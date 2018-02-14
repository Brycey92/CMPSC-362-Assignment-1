#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
# Assign IP address and port number to socket
serverSocket.bind(('', 80))
serverSocket.listen(5)

#separator = "\n---\n"
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024)
        #print message + separator
        filename = message.split()[1]
        #print "\"" + filename + "\"" + separator
        f = open(filename[1:])
        outputdata = f.read()
        #print outputdata + separator
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n").encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())    
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(("HTTP/1.1 404 Not Found\r\n\r\n").encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
