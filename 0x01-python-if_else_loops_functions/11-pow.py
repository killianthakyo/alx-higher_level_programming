#!/usr/bin python3
def pow(a, b):
    product = 1;
    for i in range(abs(b)):
        product = product * a
    if b < 0:
        product = 1 / product
    return product

