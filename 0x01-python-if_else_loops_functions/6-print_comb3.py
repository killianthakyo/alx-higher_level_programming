#!/usr/bin/python3
def determine(num):
    num = str(num)
    if len(num) < 2:
        num = "0" + num
    reversed_num = num[::-1]
    if num < reversed_num:
        return True
    else:
        return False


first = True
for i in range(0, 100):
    # determine(i)
    if determine(i):
        if first:
            print("{:0>2d}".format(i), end="")
            first = False
        else:
            print(", {:0>2d}".format(i), end="")
