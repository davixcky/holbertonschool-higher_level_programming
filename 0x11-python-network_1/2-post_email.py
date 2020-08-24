#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url, email = sys.argv[1:]
    body = {'email': email}
    data = parse.urlencode(body)
    data = data.encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
