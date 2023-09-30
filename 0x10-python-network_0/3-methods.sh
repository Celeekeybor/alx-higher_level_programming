#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -sI curl -sI "$1" | awk -F": " '/Allow:/ { print $2 }'
