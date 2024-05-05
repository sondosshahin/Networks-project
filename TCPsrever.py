import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5566))
server_socket.listen()
client_socket, client_address = server_socket.accept()
start_time = time.time()
count = 0
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    count += 1
end_time = time.time()
client_socket.close()
server_socket.close()

print(f'Time required to receive packets: {end_time - start_time} seconds')
print(f'Received {count} messages.')