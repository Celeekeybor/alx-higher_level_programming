#!/usr/bin/python3
"""takes your Github credentials (username and password)"""
import requests
from sys import argv

if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]
    r = requests.get(
        'https://api.github.com/repos/{:}/{:}/commits'.format(
            owner_name, repository_name)).json()
    if len(r) > 10:
        limit = 10
    else:
        limit = len(r)
    for item in range(limit):
        print("{:}: {:}".format(r[item].get('sha'), r[item].get(
            'commit').get('author').get('name')))
