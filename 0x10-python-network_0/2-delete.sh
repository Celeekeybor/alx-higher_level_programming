#!/bin/bash
# This script sends a `DELETE` request to the URL passed and displays the body of the response.
curl -sX DELETE "$1"
