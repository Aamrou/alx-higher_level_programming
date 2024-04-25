#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sSI "$1" |grep -Fi 'Content-Length' | rev | cut -d ' ' -f1 | rev
