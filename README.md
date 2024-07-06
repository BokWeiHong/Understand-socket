## Socket Communication Examples (Python)
This repository demonstrates basic socket communication with Python scripts:

`server.py`: Listens for connections and sends a welcome message.
`client.py`: Connects to the server and receives the message.
These scripts introduce sockets, a core concept in network programming.

## Sockets

Sockets are communication endpoints that enable applications to exchange data over networks. They provide a standardized interface, similar to electrical plugs and sockets.

## Working with Sockets

Create Sockets: Both server and client create socket objects.
Bind & Listen (Server): Server binds its socket to a port and listens for connections.
Connect (Client): Client connects to the server's hostname/port.
Data Exchange: Server and client send/receive data through their sockets.
Close Connection: Both sides close sockets when communication is done.
Running the Examples

- Install Python 3.
- Save scripts as server.py and client.py in the same directory.
- Run server first: python3 server.py
- Run client in another terminal: python3 client.py
- The client should receive the server's welcome message.

Note: These examples use TCP sockets for reliable communication. UDP sockets offer simpler, faster data transfer but are less reliable.
