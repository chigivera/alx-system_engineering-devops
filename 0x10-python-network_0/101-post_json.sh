#!/bin/bash
# Script that sends a JSON POST request with file contents
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"