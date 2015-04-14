#!/bin/bash

haveProg() {
    [ -x "$(which $1)" ]
}

if haveProg apt-get ; then
	echo apt-get
#elif haveProg yum ; then 
#	echo yum
#elif haveProg up2date ; then
#	echo up2date
else
    echo 'No package manager found!'
    exit 2
fi