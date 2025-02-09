#!/bin/bash

read -p "Entrez une valeur " a
read -p "Entrez une valeur " b

echo $((RANDOM % (b-a+1)+a))
