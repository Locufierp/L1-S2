class Maillon:
    def __init__(self, valeur=None):
        self.valeur = valeur
        self.precedent = None
        self.suivant = None

    def __str__(self):
        return str(self.valeur)

from abc import ABC, abstractmethod

class ListeChainee(ABC):
    @abstractmethod
    def est_vide(self):
        pass

    @abstractmethod
    def rechercher(self, valeur, comp=None):
        pass

    @abstractmethod
    def ajouter_debut(self, valeur):
        pass

    @abstractmethod
    def ajouter_fin(self, valeur):
        pass

    @abstractmethod
    def supprimer(self, valeur, comp=None):
        """Cette méthode doit lever une exception ValueError si la clé n’est pas présente."""
        pass

    @abstractmethod
    def supprimer_fin(self):
        pass

# Cette classe permet de rendre les listes chaînées itérables, 
# et donc d’avoir la syntaxe for maillon in liste
class ListeChaineeIterateur:
    def __init__(self,tete):
        self.__courant = tete

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__courant:
            raise StopIteration
        else:
            valeur = self.__courant.valeur
            self.__courant = self.__courant.suivant
            return valeur

class ListeDoublementChainee(ListeChainee):
    def __init__(self):
        import random
        self.__tete = None
        self.__queue = None

    def __iter__(self):
        return ListeChaineeIterateur(self.__tete)

    def __str__(self):
        s = ""
        if self.__tete is not None:
            maillon_courant = self.__tete
            while maillon_courant.suivant is not None:
                s += maillon_courant.__str__() + " -> "
                maillon_courant = maillon_courant.suivant
            s += maillon_courant.__str__()
        return s

    def est_vide(self):
        return self.__tete is None

    def rechercher(self, valeur, comp):
        if self.__tete is None:
            raise ValueError
        maillon = self.__tete 
        while maillon is not None:
            if(comp(maillon.valeur,valeur)):
                return maillon.valeur
            maillon = maillon.suivant
        raise ValueError

    def ajouter_debut(self, valeur):
        if self.__tete is None:
            M = Maillon(valeur) 
            self.__tete = M
            self.__queue = M
        else:
            M = Maillon(valeur)
            M.suivant = self.__tete
            self.__tete.precedent = M
            self.__tete = M
            if self.__queue.precedent is None:
                self.__queue.precedent = self.__tete

    def ajouter_fin(self, valeur):
        m = Maillon(valeur)
        if self.__tete == None:
            self.__tete = m
            self.__queue = m
        else:
            precedent = self.__queue
            self.__queue.suivant = m
            self.__queue = self.__queue.suivant
            self.__queue.precedent = precedent

    def supprimer(self, valeur, comp):
        maillon = self.__tete
        # Suppression en début de liste
        if(comp(maillon.valeur, valeur)):
            self.__tete = maillon.suivant
            self.__tete.precedent = None
            del maillon
        else:
            trouve = False
            while maillon.suivant is not None:
                if (comp(maillon.valeur, valeur)):
                    maillon.precedent.suivant = maillon.suivant
                    maillon.suivant.precedent = maillon.precedent
                    trouve = True
                    del maillon
                    break
                maillon = maillon.suivant
                
            # Suppression en fin de liste
            if not(trouve) and (comp(maillon.valeur, valeur)):
                maillon.precedent.suivant = maillon.suivant
                trouve = True
                del maillon

            if not(trouve):
                raise ValueError

    def supprimer_fin(self):
        if self.__tete is not None:
            if self.__tete.suivant == None:
                r = self.__tete.valeur
                self.__tete = None
                self.__queue = None
                return r
            else:
                r = self.__queue.valeur
                self.__queue.precedent.suivant = None
                self.__queue = self.__queue.precedent
                return r
