#!/usr/bin/python3
"""Script that handles HTTP errors using requests"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)