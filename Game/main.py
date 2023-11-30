from objets import Carte,JeuCartes,Player,Paquet
from menu import Menu
import pygame
pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 600))
        self.running, self.game, self.inGame = True, False, False
        self.clock = pygame.time.Clock()

        self.Menu = Menu()
        self.jeuCartes = JeuCartes()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN and not self.game:
                    self.Menu.getPLayerName(event)

    def update(self):
        if not self.game:
            self.game = self.Menu.lancer()
        else:
            if not self.inGame:
                paquet1, paquet2 = Paquet(self.jeuCartes.jeux[:26], (120, 450)), Paquet(self.jeuCartes.jeux[-26:], (1030, 50))
                self.playerEnJeu = (Player(self.Menu.names[0], paquet1), Player(self.Menu.names[1], paquet2))
                self.inGame = True
            else:
                pass

    def display(self):
        self.screen.fill('white')
        if not self.game:
            self.Menu.affiche(self.screen)
        if self.inGame:
            self.Menu.afficheInGame(self.screen, self.playerEnJeu)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.display()

            self.clock.tick(60)

game = Game()
game.run()
