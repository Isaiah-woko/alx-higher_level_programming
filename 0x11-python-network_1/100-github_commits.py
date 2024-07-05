#!/usr/bin/python3
"""Python script that list 10 commits
    (from the most recent to oldest) of the repository"""
import requests
import sys

if __name__ == "__main__":
    """Time for an interview!"""

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url, params={'per_page': 10})

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
