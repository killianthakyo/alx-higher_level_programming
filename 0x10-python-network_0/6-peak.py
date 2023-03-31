#!/usr/bin/python3
"""Method to find peak in a list of ints"""


def find_peak(list_of_integers):
    """Find peak in given list"""

    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2
    cur = list_of_integers[mid]
    if cur > list_of_integers[mid - 1] and cur > list_of_integers[mid + 1]:
        return cur
    elif cur < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
