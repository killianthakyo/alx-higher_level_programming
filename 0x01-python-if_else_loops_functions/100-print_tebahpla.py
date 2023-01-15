#!/usr/bin/python3
u = 90
letter = ''
for i in range(122, 96, -1):
    if i % 2 == 0:
        letter = chr(i)
    else:
        letter = chr(u)
    u -= 1
    print("{}".format(letter), end='')
