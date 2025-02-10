#!/bin/bash
read -p "entre un nombre " n
c=0
echo "u(0) = $n"
while [ $n -ne 1 ];
do
	c=$((c+1))
	if [ $((n%2)) == 0 ]; then
	n=$((n/2))
	else
	n=$((n*3+1))
	fi
	echo "u($c) = $n"
done
