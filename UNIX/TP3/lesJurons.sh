#!/bin/bash


nb_noms=$(cat noms |wc -l)
nb_qualificatifs=$(cat qualificatifs |wc -l)


for ligne in $(seq $nb_noms)
do
   for lignes in $(seq $nb_qualificatifs)
   do
        nom=$(cat noms|head -n $ligne|tail -n 1)
        qualificatif=$(cat qualificatifs|head -n $lignes|tail -n 1)
        Juron="$nom $qualificatif"
        echo $Juron >> lesJurons.txt
   done
done 
