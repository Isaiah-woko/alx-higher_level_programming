#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
    to the URL and displays the value of the variable
    X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    """ Response header value #1"""

    response = requests.get(sys.argv[1])
    request_id = response.headers.get("X-Request-Id")
    print(request_id)
