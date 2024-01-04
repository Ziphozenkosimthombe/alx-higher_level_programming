#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


def fetch_status():
    """status of the url & shows the response body"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == '__main__':
    fetch_status()
