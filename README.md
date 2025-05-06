# CCN-Assignment-2
# TCP vs UDP Comparison - Socket Programming Assignment

## How to Run the Programs

### TCP:
1. Open terminal 1: `python tcp_server.py`
2. Open terminal 2: `python tcp_client.py`

### UDP:
1. Open terminal 1: `python udp_server.py`
2. Open terminal 2: `python udp_client.py`

## Expected Output
- Each client sends 100 messages.
- RTT (Round Trip Time) is logged.
- TCP guarantees all packets arrive; UDP may lose some.
- UDP client may show "Timeout" messages.

## Observations

### Latency:
- **UDP** has lower latency because there's no handshake or acknowledgment.
- **TCP** is slower due to connection establishment and acknowledgments.

### Reliability:
- **TCP** ensures all messages are received in order.
- **UDP** does not guarantee delivery — packet loss occurs.

### Throughput:
- **UDP** may be faster for bulk data (if loss is acceptable).
- **TCP** introduces overhead but ensures reliability.

### Use Cases:
- **TCP**: Web browsing (HTTP), emails (SMTP), file transfers (FTP).
- **UDP**: Live streaming, gaming, VoIP, DNS.

## References
- Python's official `socket` documentation.
- Python tutorials.
- Lecture slides

