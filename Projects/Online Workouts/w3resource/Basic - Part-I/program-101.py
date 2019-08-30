# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Access and print URL contents to console.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

from http.client import HTTPConnection

if __name__ == "__main__":

    userURL = input("Enter some URL: ")
    conn = HTTPConnection("example.com")
    conn.request("GET", "/")
    result = conn.getresponse()
    # retrieves the entire contents.
    contents = result.read()
    print(contents)