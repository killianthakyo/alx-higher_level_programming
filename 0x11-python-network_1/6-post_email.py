#!/usr/bin/python3
"""Script to parse data as part of a request"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    body = {"email": argv[2]}

    res = requests.post(url, data=body)
    print(res.text)
