import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 5500

data_size = 100 * 1024
data = os.urandom(data_size)  

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:

    chunk_size = 8192 
    total_bytes_sent = 0

    for i in range(0, data_size, chunk_size):
        chunk = data[i:i + chunk_size]
        bytes_sent = client_socket.sendto(chunk, (SERVER_HOST, SERVER_PORT))
        total_bytes_sent += bytes_sent
        print(f"Sent chunk {i // chunk_size + 1}/{data_size // chunk_size} to the server.")

    print(f"Total bytes sent: {total_bytes_sent}")

    throughput_data, _ = client_socket.recvfrom(1024)
    throughput = float(throughput_data.decode())
    print(f"Throughput received from the server: {throughput:.2f} KB/s")
