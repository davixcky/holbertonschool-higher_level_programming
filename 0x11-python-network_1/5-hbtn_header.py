#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    s = requests.Session()

    response = s.get(url)
    body = response.text

    print(response.headers.get('X-Request-Id'))
