import socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_address = ('localhost', 10001)
listen_socket.bind(listen_address)
result = listen_socket.recvfrom(4096)
