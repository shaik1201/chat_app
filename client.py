import socket
# the socket has an ip and a port. it is an endpoint that recives data. it is not the comunication
# but the an endpoint.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_NET - ipv4, SOCK_STREAM - TCP

s.connect((socket.gethostname(), 1234))
# connect the client socket. params are ip and port. here we don't use the "bind" method.


full_msg = ''
while True:
    msg = s.recv(8)
    # the size of data we recieve each time.

    if len(msg) <= 0:
        break

    full_msg += msg.decode("utf-8")
    # send and recieve as bytes and then decode them.

print(full_msg)
