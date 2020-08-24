#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(response.headers['X-Request-Id'])
