#!/usr/bin/python3
"""Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to
    display your id"""
import requests
import sys

if __name__ == "__main__":
    """My GitHub!"""
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    repo = requests.get(url, auth=(username, token))
    try:
        repo.raise_for_status()
        json_ = repo.json()
        print(json_.get("id"))
    except requests.exceptions.RequestException:
        print("None")
