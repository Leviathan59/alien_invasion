import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initializing the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set.mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            #make the most recently drawn screen visisble.
            pygame.display.flip()
if __name__=='__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

