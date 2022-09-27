# import socket

# HEADERSIZE = 10


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # AF_NET - ipv4, SOCK_STREAM - TCP

# s.connect((socket.gethostname(), 1234))
# # connect the client socket. params are ip and port. here we don't use the "bind" method.


# while True:

#     full_msg = ''
#     new_msg = True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             print(f"new message length: ", msg[:HEADERSIZE])
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False

#         print(f"full message length: {msglen}")

#         full_msg += msg.decode("utf-8")
#         # send and recieve as bytes and then decode them.

#         if len(full_msg) - HEADERSIZE == msglen:
#             print("full message recieved")
#             print(full_msg[HEADERSIZE:])
#             new_msg = True
#             full_msg = ''

#     print(full_msg)







import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True