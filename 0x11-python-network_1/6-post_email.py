#!/usr/bin/python3
"""
Sends a POST request with an email parameter
then display the body
"""

import requests
import sys

if __name__ == "__main__":
    # correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # POST request with the email parameter
    response = requests.post(url, data={'email': email})

    # body of the response
    print(response.text)
