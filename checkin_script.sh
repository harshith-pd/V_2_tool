#!/bin/sh

cd $(dirname "$0") || exit 1
find . -name "__pycache__" -type d -delete
git add .
git commit -m "$1"
git push -u origin master
