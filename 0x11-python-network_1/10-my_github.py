#!/usr/bin/python3
"""script to send data to GitHub API"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=basic)
    print(res.json().get("id"))
