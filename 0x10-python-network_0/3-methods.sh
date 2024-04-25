#!/bin/bash
# This script takes in a URL and displays all HTTP methods the (accept)
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print substr($0, index($0, $2))}'
