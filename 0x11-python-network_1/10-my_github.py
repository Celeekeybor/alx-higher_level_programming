#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

# Construct the URL to fetch your GitHub user information
url = f"https://api.github.com/user"

# Set up the Basic Authentication headers using your username and access token
headers = {
    "Authorization": f"Basic {username}:{access_token}"
}

try:
    # Send a GET request to the GitHub API
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        print(None)
except requests.exceptions.RequestException as e:
    # Handle any request-related errors and print an error message
    print(None)
