#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]
then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send request and store response body size in a variable
body_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the body of the response in bytes
echo "$body_size"
