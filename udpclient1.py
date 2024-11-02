from socket import *
import time
serverName = "localhost"
serverPort = 5566
clientSocket = socket(AF_INET, SOCK_DGRAM)
str_time = time.time()
for i in range(0, 1000000):
  message = str(i)
  clientSocket.sendto(message.encode(), (serverName, serverPort))


finish_time = time.time()
required_time = finish_time - str_time
modifiedMessage,  serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

print("required time to send packets is: ", required_time, " seconds")
clientSocket.close()

