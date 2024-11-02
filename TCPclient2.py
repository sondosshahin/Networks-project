import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5566))

start_time = time.time()

for i in range(1000000):
    client_socket.send(str(i).encode())
    print(i, end='\n')

end_time = time.time()
client_socket.close()

print(f'Time required to send packets: {end_time - start_time} seconds')