#!/bin/bash

URL="$1"

if [ -z "$URL" ]
then
  echo "Usage: $0 <URL>"
  exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$response" == "200" ]
then
  curl -s "$URL"
fi
