#!/usr/bin/python3

import socket

# Create a TCP socket (client-side)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server hostname (localhost in this case)
host = socket.gethostname()

# Port to connect to
port = 444

# Connect to the server
clientsocket.connect((host, port))

# Receive data from the server (up to 1024 bytes)
message = clientsocket.recv(1024)

# Close the connection
clientsocket.close()

# Decode and print the received message (assuming ASCII encoding)
print(message.decode("ascii"))
