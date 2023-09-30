#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST
"""
import requests
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

try:
    # Send a POST request to the specified URL with the email parameter
    response = requests.post(url, data=data)
    # Display the response body
    print("Your email is:", response.text)
except requests.exceptions.RequestException as e:
    # Handle any request-related errors and print an error message
    print("Error:", e)

