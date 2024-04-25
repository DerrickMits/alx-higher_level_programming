#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the UR
#The header variable X-School-User-Id, and displays the body of the response
curl "$1" -sX GET -H "X-School-User-Id:98
