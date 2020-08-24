#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests
from sys import argv


if __name__ == '__main__':
    url, email = argv[1:]
    s = requests.Session()

    data = {'email': email}
    response = s.post(url, data=data)
    body = response.text
    print(body)
