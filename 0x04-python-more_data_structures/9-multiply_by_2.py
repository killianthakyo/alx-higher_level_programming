#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        for key, val in a_dictionary.items():
            new_dict.update({key: val * 2})
        return (new_dict)
