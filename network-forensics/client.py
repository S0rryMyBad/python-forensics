#!/usr/bin/python2

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8080

# connection to hostname on the port
s.connect((host, port))

# receive no more than 1024 bytes
tm = s.recv(1024)
print("the client is waiting for connection")
s.close()
