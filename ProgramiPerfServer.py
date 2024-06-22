import socket
import time

HOST = 'localhost'
PORT = 5500

BUFFER_SIZE = 8192

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print("Server is waiting for data...")

    data_received = 0
    start_time = time.time()

    while data_received < 100 * 1024:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        data_received += len(data)

    end_time = time.time()
    time_taken = end_time - start_time

    throughput = (data_received / 1024) / time_taken
    print(f"Received {data_received} bytes in {time_taken} seconds.")
    print(f"Throughput: {throughput:.2f} KB/s")

    server_socket.sendto(str(throughput).encode(), addr)
