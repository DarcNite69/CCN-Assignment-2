import socket
import time

HOST = '127.0.0.1'
PORT = 5001

total_time = 0
total_data_sent = 0  # Variable to track total data sent

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    for i in range(100):
        message = f"Message {i+1}"
        start = time.time()
        client.sendall(message.encode())
        data = client.recv(1024)
        end = time.time()
        
        rtt = end - start
        total_time += rtt
        total_data_sent += len(message)  # Add the length of each message to total data sent
        
        print(f"Sent: {message} | Received: {data.decode()} | RTT: {rtt:.6f} sec")
        
        with open("tcp_log.txt", "a") as log:
            log.write(f"{rtt:.6f} sec RTT\n")

# Calculate average RTT
average_rtt = total_time / 100
# Calculate throughput in bytes per second (Bps)
throughput = total_data_sent / total_time

print(f"\nAverage RTT: {average_rtt:.6f} sec")
print(f"Throughput: {throughput:.2f} bytes/sec")
