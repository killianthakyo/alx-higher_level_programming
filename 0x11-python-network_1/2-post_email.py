#!/usr/bin/python3
"""Script that takes in a URL and an email"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    body_dict = {"email": argv[2]}
    body = urllib.parse.urlencode(body_dict).encode("ascii")

    req = urllib.request.Request(url, body)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print(html.decode("utf-8"))
