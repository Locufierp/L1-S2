#!/bin/bash
read -p " écris un mot " mot
longueur=${#mot}
echo "longueur du $mot : $longueur"
for i in $(seq $longueur);
do 
	lettre=$(echo $mot | cut -c $i)
	echo "lettre numero $i : $lettre"
done
