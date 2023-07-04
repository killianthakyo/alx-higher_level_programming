#!/usr/bin/python3
"""Script to send requestusing requests"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
