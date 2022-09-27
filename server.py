import socket
# the socket has an ip and a port. it is an endpoint that recives data. it is not the comunication
# but an endpoint.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_NET - ipv4, SOCK_STREAM - TCP

s.bind((socket.gethostname(), 1234))
# bind the socket to a server. the server is on the same machine so it is just localhost. 1234 is port.

s.listen(5)
# queue of 5.

while True:
    clientsocket, address = s.accept()
    # accept whoever wants to connect. the clientsocket is a foreign socket object.

    print(f"connection from {address} has been established.")
    clientsocket.send(bytes("welcome to the server", "utf-8"))
    clientsocket.close()
