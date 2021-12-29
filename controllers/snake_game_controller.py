from settings import settings
from views.snake_game_window import SnakeGameWindow

import pygame

class SnakeGameController:
    def __init__(self):
        self._game = pygame

        self._run = True
        self._clock = self._game.time.Clock()
        self._display = SnakeGameWindow(self._game, "Snake Game", 900, 500)

    def start(self):
        while self._run:
            self._clock.tick(settings['fps'])
            for event in self._game.event.get():
                print(event.type)
                if event.type == self._game.QUIT:
                    self._run = False
                self._display.render()
        self._game.quit()

    