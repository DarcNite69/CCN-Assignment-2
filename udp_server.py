import socket
import random

HOST = '127.0.0.1'
PORT = 5002
DROP_RATE = 0.2  # 20% of packets will be dropped

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")
    for _ in range(100):
        data, addr = server.recvfrom(1024)
        if random.random() > DROP_RATE:
            response = f"Received: {data.decode()}"
            server.sendto(response.encode(), addr)
