#!/usr/bin/python3
"""Script that displays X-Request-Id header using requests"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))