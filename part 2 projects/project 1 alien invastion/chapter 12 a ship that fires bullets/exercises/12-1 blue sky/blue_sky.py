#!/usr/bin/env python3

# 12-1 Blue Sky: Make a Pygame window with a blue background

import sys
import pygame

from settings import Settings

class BlueSky:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the background color.
        self.bg_color = (0, 0, 255)
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        """Start the main loop for the game."""
        # Watch for keyboard and mouse events
        while True:
            self._check_events()

    def _check_events(self):
        """Responds to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        
        
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()