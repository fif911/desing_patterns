# https://pymotw.com/3/socket/uds.html#communication-between-parent-and-child-processes
# By default, a UDS socket is created, but the caller can also pass address family, socket type, and even protocol
# options to control how the sockets are created.
# socket_socketpair.py
# NOTE: THIS WILL NOT WORK ON WINDOWS CAUSE os.fork is not supported in Windows
import socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print('in parent, sending message')
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print('response from child:', response)
    parent.close()

else:
    print('in child, waiting for message')
    parent.close()
    message = child.recv(1024)
    print('message from parent:', message)
    child.sendall(b'pong')
    child.close()
