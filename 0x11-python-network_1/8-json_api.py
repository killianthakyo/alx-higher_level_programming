#!/usr/bin/python3
"""send request data in a variable"""
from sys import argv
import requests

if __name__ == "__main__":
    if not argv[1]:
        val = ""
    else:
        val = argv[1]
    body = {"q": val}

    res = requests.post("http://0.0.0.0:5000/search_user", data=body)
    try:
        res_json = res.json()
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
