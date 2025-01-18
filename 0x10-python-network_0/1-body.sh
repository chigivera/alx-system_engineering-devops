#!/bin/bash
# Script that displays body of 200 status code response
curl -s -w "%{http_code}" "$1" | grep -x "200" > /dev/null && curl -s "$1"