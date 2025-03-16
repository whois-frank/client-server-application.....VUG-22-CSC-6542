import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_address = ('localhost', 12345)  # Use any available port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on", server_address)

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive data from client
    data = client_socket.recv(1024).decode()
    print(f"Received from client: {data}")

    # Send response
    response = "Message received!"
    client_socket.send(response.encode())

    # Close connection
    client_socket.close()
