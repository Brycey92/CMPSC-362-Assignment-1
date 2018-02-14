# UDPPinger.py
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1, 11):
    timeBefore = time.time()
    clientSocket.sendto(("Ping " + str(i) + " " + str(time.strftime("%H:%M:%S"))).encode(), ("127.0.0.1", 12000))

    try:
        msg, serverAddress = clientSocket.recvfrom(1024)
        timeAfter = time.time()
        print('Data: ', msg)
        print('RTT:  ', timeAfter - timeBefore)
    except:
        print('Request timed out')
