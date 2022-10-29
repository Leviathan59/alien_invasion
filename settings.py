class Settings:
    bg_color = (230, 230, 230)
    screen_width = 1200
    screen_height = 800

    ship_speed = .5
    bullet_speed = 1.0
    bullet_width = 3
    bullet_height = 15
    bullet_color = (60, 60, 60)
    bullets_allowed = 3
    """A class to store all settings for Alien Invasion"""

def __init__(self):
    """Initialize the game's settings."""

    # Screen Settings
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)

    #Ship Settings
    self.ship_speed = 1.5
    self.ship_limit = 3

    # Bullet settings
    self.bullet_speed = 1.5
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60,60,60)
    self.bullets_allowed = 3

    # Alien Settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    #fleet direction of 1 represents right, -1 represents left
    self.fleet_direction = 1