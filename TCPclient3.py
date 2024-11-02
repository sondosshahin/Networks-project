import socket
import time
serverIP="192.168.0.105"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.105', 5566))

start_time = time.time()

for i in range(1000000):
    client_socket.send(str(i).encode())
    print(i, end='\n')

end_time = time.time()
client_socket.close()

print(f'Time required to send packets: {end_time - start_time} seconds')v