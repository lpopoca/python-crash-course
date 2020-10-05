#!/usr/bin/env python3

# 12-2. Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap. Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen, or vice versa.

import sys
import pygame

from settings import Settings
from character import Character

class GameCharacter:
    """Overll class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.display.set_caption("Game Character")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))

        # Set the background color.
        self.bg_color = self.settings.bg_color

        self.character = Character(self)

        # Flag for game running
        self.game_running = True

    def main_loop(self):
        """Start the main loop for the game."""
        while self.game_running:
            self._check_events()
            self.character.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    gc = GameCharacter()
    gc.main_loop()
