import pygame

class Character:
    """A class to manage the character."""
    def __init__(self, gc_game):
        """Initialize the character and set its starting posistion."""
        self.screen = gc_game.screen
        self.settings = gc_game.settings
        self.screen_rect = gc_game.screen.get_rect()

        #Load the character image and get its rect
        self.image = pygame.image.load('part 2 projects\\project 1 alien invastion\\chapter 12 a ship that fires bullets\exercises\\12-2 game character\\images\\character.bmp')
        self.rect = self.image.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the character's horizontal position.
        self.x = float(self.rect.x)

        # Store a decimal value for the character's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Update the character's postion."""

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)