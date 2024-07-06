#!/usr/bin/python3

# Import for network communication
import socket

# Create a TCP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get server hostname (can be IP address)
host = socket.gethostname()

# Port to listen on
port = 444

# Bind socket to host and port
serversocket.bind((host, port))

# Start listening (max 3 queued connections)
serversocket.listen(3)

# Continuously accept connections
while True:
    # Accept a connection from a client
    clientsocket, address = serversocket.accept()

    print(f"Connected from {address}")
    message = 'Thank you for connecting to the server\r\n'

    # Send message (encoded in ASCII)
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()