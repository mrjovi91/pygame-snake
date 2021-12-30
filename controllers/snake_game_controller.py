from settings import settings
from views.snake_game_window import SnakeGameWindow
from models.cell import Cell

import pygame
from time import sleep

class SnakeGameController:


    def __init__(self):
        self._game = pygame
        self._run = True
        self._clock = self._game.time.Clock()
        
        self.rows = 40
        self.columns = 40
        self._grid = []
        for y in range(0,self.rows):
            row = []
            for x in range(0,self.columns):
                row.append(Cell(x, y))
            self._grid.append(row)

        self._snake = [[int(self.rows/2), int(self.columns/2)]]
        self._grid[self._snake[0][0]][self._snake[0][1]].head = True
        self._direction = 'right'



        self._display = SnakeGameWindow(self._game, "Snake Game", 1200, 1200, self.rows, self.columns)

    def start(self):
        while self._run:
            self._display.refresh(self._grid)
            self._clock.tick(settings['fps'])
            sleep(0.25)
            for event in self._game.event.get():
                if event.type == self._game.QUIT:
                    self._run = False
            keys_pressed = self._game.key.get_pressed()
            if keys_pressed[self._game.K_w]:
                self._direction = 'up'
            elif keys_pressed[self._game.K_d]:
                self._direction = 'right'
            elif keys_pressed[self._game.K_s]:
                self._direction = 'down'
            elif keys_pressed[self._game.K_a]:
                self._direction = 'left'

            self.move()
        self._game.quit()

    
    def move(self):
        directions = {
            'up': [-1, 0],
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1]
        }
        
        current_head = self._grid[self._snake[0][0]][self._snake[0][1]]
        new_head_coordinates = [self._snake[0][0] + directions[self._direction][0], self._snake[0][1] + directions[self._direction][1]]
        new_head = self._grid[new_head_coordinates[0]][new_head_coordinates[1]]
        current_head.head = False
        new_head.head = True
        self._snake[0] = new_head_coordinates
        