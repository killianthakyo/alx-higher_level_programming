#!/bin/bash
# Script  to send a request to a URL and display body size of response
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
