#!/usr/bin/python3
"""Script that uses GitHub API to display user id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, token)
    
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))