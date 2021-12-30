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

        self._grid[5][10].food = True
        self._grid[5][13].food= True
        self._grid[5][8].food = True

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
        grow = False

        for snake_part_coordinates in self._snake:
            snake_part = self._grid[snake_part_coordinates[0]][snake_part_coordinates[1]]

            snake_part_coordinates[0] = self._snake[0][0] + directions[self._direction][0]
            snake_part_coordinates[1] = self._snake[0][1] + directions[self._direction][1]
            if snake_part.head:
                if snake_part.food:
                    grow = True
                    snake_part.food = False
                new_head = self._grid[snake_part_coordinates[0]][snake_part_coordinates[1]]
                new_head.head = True
                snake_part.head = False
                snake_part.body = True

        if not grow:
            if len(self._snake) > 1:
                current_tail_coordinates = self._snake[-1]
                current_tail = self._grid[current_tail_coordinates[0]][current_tail_coordinates[1]]
                current_tail.body = False
                self._snake.remove(current_tail_coordinates)

            
        