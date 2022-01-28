from sockets.python3.client import Client
import socket
socket.pa

client = Client()
response, addr = client.poll_server("Hello world", server=('127.0.0.1', 11113))
print(response, addr)
