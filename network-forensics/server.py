#!/usr/bin/python2

import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8080

# bind to the port
serversocket.bind((host, port))

# queue up to 10 request
serversocket.listen(10)

while True:
    # estabilish a connection
    clientsocket, addr = serversocket.accep()

    print("got a connection from %s", % str(addr))

    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
