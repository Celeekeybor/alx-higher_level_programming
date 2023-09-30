#!/bin/bash
# This script takes a URL passed as a parameter and displays the response body size.
curl -sI "$1" | awk -F" " '/Content-Length/ { print $2 }'
