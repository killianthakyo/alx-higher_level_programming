#!/usr/bin/python3
"""Script that takes in a URL and
displays the X-Request-Id in the response"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
