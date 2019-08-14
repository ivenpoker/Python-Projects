# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Get current terminal window on which program it run.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 14, 2019                                          #
#                                                                                 #
###################################################################################

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
                                   fcntl.ioctl(0, termios.TIOCGWINSZ,
                                               struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th


if __name__ == "__main__":
    print(f"Number of columns and Rows: {terminal_size()}")
