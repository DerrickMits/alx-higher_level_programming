#!/bin/bash
# sends a JSON POST request to a URL passed , and displayed
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
