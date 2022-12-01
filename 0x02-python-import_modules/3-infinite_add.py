#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)

    sum = 0
    for i in range(1, arg_count):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
