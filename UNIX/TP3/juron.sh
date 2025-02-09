#!/bin/bash


nb_noms=$(cat noms |wc -l)
nb_qualificatifs=$(cat qualificatifs |wc -l)

nom_hasard=$((RANDOM % nb_noms +1))
qualificatif_hasard=$((RANDOM % nb_qualificatifs +1))

nom=$(cat noms|head -n $nom_hasard|tail -n 1)
qualificatif=$(cat qualificatifs|head -n $qualificatif_hasard|tail -n 1)

echo "Juron: $nom $qualificatif"
