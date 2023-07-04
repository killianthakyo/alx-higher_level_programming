#!/usr/bin/python3
"""Script to get commits by a user"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
          argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    if len(commits) > 10:
        for i in range(10):
            print("{}: {}".format(
                  commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    else:
        for i in range(len(commits)):
            print("{}: {}".format(
                  commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
