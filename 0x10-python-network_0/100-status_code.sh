#!/bin/bash
# sends a request to a URL passed as an argument and displays(Code)
curl -s -o /dev/null -w "%{http_code}" "$1"
