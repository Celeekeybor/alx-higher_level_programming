#!/bin/bash
# This script sends a `GET` request to the URL passed along with a header variable `X-HolbertonSchool-User-Id` with value `98`
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
