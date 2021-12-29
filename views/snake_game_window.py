from libs.colors import *

class SnakeGameWindow:
    def __init__(self, game, title, width, height):
        self._game = game
        self._title = title
        self._width, self._height = width, height
        self._window = self._game.display.set_mode((self._width, self._height))
        self._game.display.set_caption(self._title)
        
    def render(self):
        self._window.fill(BLACK)
        self._game.draw.rect(self._window, WHITE, self._game.Rect(self._width/2 - 90/2, self._height/2 - 60/2, 90, 60))  
        self._game.display.update()