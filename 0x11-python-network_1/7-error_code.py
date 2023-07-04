#!/usr/bin/python3
"""Error handling in a request"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
