#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""

    s = requests.Session()

    data = {'q': letter}
    response = s.post(url, data=data)
    try:
        body = response.json()
        if body == {}:
            msg = 'No result'
        else:
            msg = '[{}] {}'.format(body['id'], body['name'])
    except ValueError:
        msg = 'Not a valid JSON'

    print(msg)
