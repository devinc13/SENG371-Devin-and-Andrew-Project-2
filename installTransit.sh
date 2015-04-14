#!/bin/bash
# Run this script with sudo!

curl -L https://static.rust-lang.org/rustup.sh | sh
if [ "$?" = "0" ]; then
	git clone https://github.com/Hoverbear/transit.git
	if [ "$?" = "0" ]; then
		pkgManager=getPackageManager.sh
		if [ "$?" = "0" ]; then
			$pkgManager install cargo
			cd transit
			cargo build --release
			cd ..
			if [ "$?" = "0" ]; then
				echo "Transit installed successfully!"
			else
				echo "Could not compile Transit."
				exit 2
			fi
		else
			echo "No compatible package Manager detected."
			exit 2
		fi
	else
		echo "Could not clone the Transit repo."
		exit 2
	fi
else
	echo "Could not download and/or install Rust."
	exit 2
fi
