#!/bin/bash

havePkgMngr ()
{
	[ -x "$(which $1)" ]
}

if havePkgMngr apt-get ; then
	echo apt-get
elif havePkgMngr yum ; then
	echo yum
elif havePkgMngr brew ; then
	echo brew
elif havePkgMngr up2date ; then
	echo up2date
else
	echo "No package manager found!"
	exit 2
fi