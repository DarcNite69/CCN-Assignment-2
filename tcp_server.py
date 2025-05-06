import socket
import time

HOST = '127.0.0.1'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"TCP Server listening on {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
        for _ in range(100):
            start = time.time()
            data = conn.recv(1024)
            if not data:
                break
            response = f"Received: {data.decode()}"
            conn.sendall(response.encode())
            end = time.time()
            with open("tcp_log.txt", "a") as log:
                log.write(f"{end - start:.6f} sec RTT\n")
