#!/usr/bin/python3
def f(integ):
    return chr(integ)


# Print the ASCII alphabet, in lowercase, not followed by a new line.
for i in range(97, 123):
    if f(i) != 'q' and f(i) != 'e':
        print("{}".format(chr(i)), end="")
