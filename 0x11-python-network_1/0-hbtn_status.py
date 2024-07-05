#!/usr/bin/python3
"""Function for task What's my status? #0"""
import urllib.request


def fetch_status():
    """ a Python script that fetches a url"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:
        html = response.read()
        # print(html)
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
