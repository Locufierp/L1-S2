#!/bin/bash
read -p "entre un nombre " n1
read -p "entre un deuxieme nombre " n2

for u0 $(seq n1 , n2);
do
	if [ $((n1 -ge n2)) ]; then
