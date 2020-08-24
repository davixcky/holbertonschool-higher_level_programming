#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    repo, user = argv[1:]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)

    s = requests.Session()

    response = s.get(url)
    data = response.json()
    for i in range(10):
        obj = data[i]
        print(obj.get('sha'), end=': ')
        print(obj.get('commit').get('author').get('name'))
