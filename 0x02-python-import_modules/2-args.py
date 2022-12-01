#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    if arg_count == 1:
        print("{} argument:". format(arg_count))
    elif arg_count == 0:
        print("{} arguments.". format(arg_count))
    else:
        print("{} arguments:". format(arg_count))

    for i in range(1, arg_count + 1):
        print("{}: {}".format(i, sys.argv[i]))
