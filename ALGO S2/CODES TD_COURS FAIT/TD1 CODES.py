# Créé par olivi, le 21/01/2025 en Python 3.7
#TD 1.1

def imagevide(longueur, hauteur ):
    image = []
    for i in range(hauteur):
        image.append([])
        for j in range(longeur):
            image[i].append(0)
    return image

def imageseuiller(S, image , longeur , hauteur ):
    seuil = imagevide(hauteur , longeur)
    for i , ligne in enumerate(image):
        for j , pixel in enumerate(ligne):
            if pixel <= S:
                valeur = 0
            else:
                valeur = 65536
            seuil [i][j] = valeur


