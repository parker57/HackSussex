#!/usr/bin/env bash

file="found.txt"
if [ -f $file ] ; then
	rm $file
fi

python runner.py "$@" >> found.txt

cat found.txt

cat found.txt | while read line
do
	xdg-open $line
done

