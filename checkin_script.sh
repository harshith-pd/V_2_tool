#!/bin/sh

cd $(dirname "$0") || exit 1
git add .
git commit -m "$1"
git push -u origin master
