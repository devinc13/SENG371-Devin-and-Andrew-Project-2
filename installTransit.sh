#!/bin/bash
#Run as sudo!!

curl -L https://static.rust-lang.org/rustup.sh | sh
if [ "$?" = "0" ]; then
	git clone https://github.com/Hoverbear/transit.git
	if [ "$?" = "0" ]; then
		cd transit
		cargo build --release #--verbose
		cd ..
		chmod -R a+w transit
	else
		echo "Could not clone the Transit repo."
		exit 2
	fi
else
	echo "Could not download and/or install Rust."
	exit 2
fi
