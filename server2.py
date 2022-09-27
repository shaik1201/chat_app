# in this one we use header to tell the size of the data that is coming. by that the the server
# will wait for all of the data to arrive and then will wait to another message.

import socket

HEADERSIZE = 10


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

    msg = "welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    # '<' means left aligned when completing the string to the HEADERSIZE.

    clientsocket.send(bytes(msg, "utf-8"))

