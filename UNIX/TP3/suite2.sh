#!/bin/bash

u0=$1 
a=$2
b=$3
n=$4


u=$u0

for i in $(seq $n)
do
  u=$((a*u+b))
  printf "%d; " $u
done
 
