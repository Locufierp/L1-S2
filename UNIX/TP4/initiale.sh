#!/bin/bash

while true; do
    # Demander à l'utilisateur de saisir une chaîne de caractères
    read -p "Entrez une chaîne de caractères (ou 'stop' pour quitter) : " input

    # Vérifier si l'utilisateur a entré "stop"
    if [ "$input" = "stop" ]; then
        echo "Fin du script. Au revoir !"
        break
    fi

    # Récupérer la première lettre de la chaîne
    initiale=$(echo "$input" | cut -c1)

    # Afficher un message adapté à l'initiale
    case $initiale in
        [A-Z])
            echo "Majuscule"
            ;;
        [a-z])
            echo "miniscules"
            ;;
        [0-9])
            echo "chifre"
            ;;
        *)
            echo "bizarre"
            ;;
    esac
done
