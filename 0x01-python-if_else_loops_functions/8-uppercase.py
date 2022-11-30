#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        if ord(str[i]) <= 122 and ord(str[i]) >= 97:
            # CONVERT TO UPPER BY -32
            ch_r = chr(ord(str[i])-32)
        else:
            ch_r = str[i]

        if i != length - 1:
            print("{}".format(ch_r), end="")
        else:
            print("{}".format(ch_r))
