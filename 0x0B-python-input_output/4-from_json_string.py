#!/usr/bin/python3
"""
Return JSON object
"""


import json


def from_json_string(my_str):
    """
    Return JSON OBJECT
    """
    return(json.loads(my_str))
