#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if number < 0 and last_digit != 0:
    last_digit = -abs(last_digit)
if last_digit > 5:
    status = "and is greater than 5"
elif last_digit == 0:
    status = "and is 0"
else:
    status = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, status))
