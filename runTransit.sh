#!/bin/bash

echo "Locating transit"
transit="./transit/target/release/transit"
if [ -x transit ]; then
	if [ -n "$2" ]; then
	    repo="$2"
	    git clone $repo
	    if [ "$?" = "0" ]; then
	        transit $repo > output.json
	        python transitParser.py -f output.json
	    else
	        echo "Could not clone the repo. You may want to try cloning it yourself first."
	    fi
    else
    	echo "Invalid input"
    	exit 2
else
    echo "Could not locate Transit. Did you run installTransit.sh yet?"
    exit 2
fi
