#!/usr/bin/python3
"""
Sends a POST request with an email parameter
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Make a POST request with the email parameter
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)
