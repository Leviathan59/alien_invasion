import pygame

class Rocket:

    def __init__(self, ai_game):
        pygame.init()
        self.character = pygame.image.load('../images/ship_0014.png')
        self.rect = self.character.get_rect()
        self.rocket_speed = 1.5

        screen_rect = screen.get_rect()
        self.screen = pygame.display.set_mode((1000,1000))
        self.rect.center = self.screen.get_rect().center
        self.screen_rect = screen.get_rect()

        # Store a decimal value for the rocket's horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.character, self.rect)

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('RocketGame')
rocket = Rocket(screen)

while True:
    for event in pygame.event.get():
        if event.type == 768:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            if event.key == pygame.K_UP:
                rocket.moving_up = True
            if event.key == pygame.K_DOWN:
                rocket.moving_down = True
            if event.key == pygame.K_LEFT:
                rocket.moving_left = True
        if event.type == 769:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            if event.key == pygame.K_UP:
                rocket.moving_up = False
            if event.key == pygame.K_DOWN:
                rocket.moving_down = False
            if event.key == pygame.K_LEFT:
                rocket.moving_left = False



    rocket.update()
    screen.fill((0, 0, 200))
    rocket.blitme()
    pygame.display.flip()

# draw the character


 # Moves character to center

# draw ("blit") the character graphic on the screen