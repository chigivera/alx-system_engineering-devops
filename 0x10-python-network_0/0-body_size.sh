#!/bin/bash
# Script that displays the size of the response body in bytes
curl -s "$1" | wc -c