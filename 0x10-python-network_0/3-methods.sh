#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sI "$1" |grep -Fi 'Allow:' | cut -d $' ' -f2-
