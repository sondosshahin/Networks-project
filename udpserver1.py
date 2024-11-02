from socket import *
import time

serverPort = 5566
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("The server is ready to receive")
start_time = time.time()
counter = 0
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    counter = counter+1
    modifiedMessage = message.decode()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("counter = ", counter)
end_time = time.time()
req_time = start_time - end_time
print("required time to receive packets is: ", req_time, " seconds")




