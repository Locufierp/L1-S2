#!/bin/bash

read -p "Valeur de u" u0
read -p "Valeur de a" a
read -p "Valeur de b" b
read -p "Combien de termes voulez vous calculer" n


u=$u0

for i in $(seq $n)
do
  u=$((a*u+b))
  printf "%d; " $u
done

