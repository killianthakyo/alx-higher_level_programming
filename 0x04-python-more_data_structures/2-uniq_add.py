#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = sorted(set(my_list))
    total = 0
    for i in new_list:
        total = total + i
    return total
