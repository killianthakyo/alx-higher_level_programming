#!/usr/bin/python3
"""Script taht takes in a URL, sends a request
and displays the body of the response"""
from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
