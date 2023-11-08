from objets import Carte,JeuCartes,Player,Paquet

class Game:
    def __init__(self):
        self.jeuCartes = JeuCartes()
        self.running = True

    def distribuer(self):
        paquet1, paquet2 = Paquet(self.jeuCartes.jeux[:26]), Paquet(self.jeuCartes.jeux[-26:])
        self.playerEnJeu = (Player(input("Saissisez le nom du Joueur 1 : "), paquet1), Player(input("Saissisez le nom du Joueur 2 : "), paquet2))
        print()

    def bataille(self, j, k):
        for player in self.playerEnJeu:
            if j == 0:
                input(f"{player.nom} appuyer sur entree pour tirer une carte : ")
            else:
                input(f"{player.nom} appuyer sur entree pour re-tirer une carte : ")

            carteTirer = player.tirer()
            self.carteEnJeu.append(carteTirer)
            print(f"Vous avez tirer la carte {carteTirer}\n")

        if self.carteEnJeu[j].v > self.carteEnJeu[k].v:
            print(f"{self.carteEnJeu[j]} > {self.carteEnJeu[k]}\n")
            return 0
        elif self.carteEnJeu[j].v < self.carteEnJeu[k].v:
            print(f"{self.carteEnJeu[j]} < {self.carteEnJeu[k]}\n")
            return 1

        elif self.carteEnJeu[j].v == self.carteEnJeu[k].v:
            print(f"{self.carteEnJeu[j]} = {self.carteEnJeu[k]} \nBataille !!!\n\n")
            return self.bataille(j+2, k+2)

    def run(self):
        self.jeuCartes.shuffle()
        self.distribuer()

        while self.running:
            self.carteEnJeu = []
            playerGagnant = self.bataille(0, 1)

            print(f"{self.playerEnJeu[playerGagnant].nom} a gagner : ", end='')
            for carte in self.carteEnJeu:
                print(carte, end=' ')
                self.playerEnJeu[playerGagnant].paquet.ajouter(carte)
            print()
            print(f"{self.playerEnJeu[0].nom} : {len(self.playerEnJeu[0].paquet.paquet)} | {self.playerEnJeu[1].nom} : {len(self.playerEnJeu[1].paquet.paquet)}")
            print('\n\n')


game = Game()
game.run()
