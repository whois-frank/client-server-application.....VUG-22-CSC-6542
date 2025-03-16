import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)  # Same port as the server
client_socket.connect(server_address)

# Send a message
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

# Close the connection
client_socket.close()
