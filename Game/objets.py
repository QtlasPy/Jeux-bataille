import random

class Carte:
    def __init__(self, v, f):
        self.v = v
        self.f = f

    def __str__(self):
        carte_utf = {'pique' : [chr(i) for i in range(127137, 127151) if i != 127148],
                    'coeur' :  [chr(i) for i in range(127153, 127167) if i != 127164],
                    'carreau' : [chr(i) for i in range(127169, 127183) if i != 127180],
                    'trefle' : [chr(i) for i in range(127185, 127199) if i != 127196]
                    }
        return carte_utf[self.f][self.v]


class JeuCartes:
    def __init__(self):
        self.jeux = [Carte(v, f) for f in  ("pique", 'coeur', "carreau", "trefle") for v in range(0, 13)]

    def shuffle(self):
        random.shuffle(self.jeux)

    def __str__(self):
        affiche = ""
        for j in range(0, 4):
            for carte in range(13*j, 13*j+13):
                    affiche += self.jeux[carte].__str__() + ' '
            affiche += '\n'


        return affiche

class Paquet:
    def __init__(self, cartes):
        self.paquet = cartes

    def ajouter(self, x):
        self.paquet.insert(0, x)


class Player:
    def __init__(self, nom, paquet):
        self.paquet = paquet
        self.nom = nom

    def tirer(self):
        carteTirer = self.paquet.paquet.pop(len(self.paquet.paquet) - 1)
        return carteTirer

    def __str__(self):
        affiche = self.nom  + ' : '
        for carte in self.paquet.paquet:
            affiche += carte.__str__() + ' '
        return affiche
