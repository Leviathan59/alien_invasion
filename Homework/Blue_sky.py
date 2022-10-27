import pygame
import time

screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 200))
pygame.display.flip()

#draw the character
character = pygame.image.load('../images/ship_0014.png')

character_rect = character.get_rect()
screen_rect = screen.get_rect()
character_rect.center = screen_rect.center #Moves character to center

#draw ("blit") the character graphic on the screen
screen.blit(character, character_rect)

pygame.display.flip()
time.sleep(5)

class ship:

    def __init__(self, ai_game):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the rocket's horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
     self.screen.blit(self.image, self.rect)


