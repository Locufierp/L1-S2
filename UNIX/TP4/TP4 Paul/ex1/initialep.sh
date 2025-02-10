#!/bin/bash
while true;
do 
read -p "chaine de caractere" ch
	if [ $ch = "stop" ] ; then 
		break;
	fi 
done
