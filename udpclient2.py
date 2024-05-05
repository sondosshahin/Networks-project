from socket import *
import time
clientIP = "192.168.68.114"
serverIP = "192.168.68.101"
serverPort = 5566
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverIP,serverPort))
str_time = time.time()
for i in range(0, 1000000):
  message = str(i)
  clientSocket.sendto(message.encode(), (serverIP, serverPort))


finish_time = time.time()
required_time = finish_time - str_time
modifiedMessage,  serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

print("required time to send packets is: ", required_time, " seconds")
clientSocket.close()