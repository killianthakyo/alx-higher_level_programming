#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
signed = ""
if number < 0:
    signed = "-"
if last_digit > 5:
    status = "and is greater than 5"
elif last_digit == 0:
    status = "and is 0"
else:
    status = "and is less than 6 and not 0"

print("Last digit of {} is {}{} {}".format(number, signed, last_digit, status))
