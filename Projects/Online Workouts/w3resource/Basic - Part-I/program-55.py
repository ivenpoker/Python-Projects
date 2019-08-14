# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Find local IP addresses using Python's stdlib            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 10, 2019                                          #
#                                                                                 #
###################################################################################

if __name__ == "__main__":
    import socket
    print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                     s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                                                                                                                 socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
