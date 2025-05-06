import socket
import time

HOST = '127.0.0.1'
PORT = 5002
TIMEOUT = 1.0  # 1 second timeout for receiving

total_time = 0
received = 0

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(TIMEOUT)
    for i in range(100):
        message = f"Message {i+1}"
        start = time.time()
        client.sendto(message.encode(), (HOST, PORT))
        try:
            data, _ = client.recvfrom(1024)
            end = time.time()
            rtt = end - start
            total_time += rtt
            received += 1
            print(f"Sent: {message} | Received: {data.decode()} | RTT: {rtt:.6f} sec")
            with open("udp_log.txt", "a") as log:
                log.write(f"{rtt:.6f} sec RTT\n")
        except socket.timeout:
            print(f"Sent: {message} | Timeout - No Response")
            with open("udp_log.txt", "a") as log:
                log.write("Timeout\n")

if received > 0:
    avg_rtt = total_time / received
    throughput = received / total_time
    loss_rate = (100 - received) / 100
    print(f"\nAverage RTT: {avg_rtt:.6f} sec")
    print(f"Packet Loss Rate: {loss_rate:.2%}")
    print(f"Throughput: {throughput:.2f} msg/sec")
else:
    print("\nAll packets lost.")
