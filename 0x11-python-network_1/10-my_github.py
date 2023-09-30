#!/usr/bin/python3
"""takes your Github credentials 
"""
import requests
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    try:
        r = requests.get('https://api.github.com/user', auth=(
            argv[1], argv[2])).json()
        print(r.get('id'))
    except:
        print("None")
