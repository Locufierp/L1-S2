#! /bin/bash

noms=$(cat noms| wc -l )
nb2=$(cat qualificatifs | wc -l)
rand_nom=$((RANDOM % noms + 1))
rand_q=$((RANDOM % nb2 + 1 ))
res=$(cat noms | head -n $rand_nom | tail -n 1)
resq=$( cat nb2 | head -n $rand_q | tail -n 1 )
echo"$res $resq"
