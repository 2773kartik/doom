import pygame as pg

import random

def generate_map(width, height):
    # Initialize the map with walls (1)
    map = [[1 for _ in range(width)] for _ in range(height)]

    # Create open spaces (0) within the map
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            map[i][j] = 0

    # Add random obstacles (1) to the map
    for _ in range(int(width * height * 0.2)):  # 20% of the map will be obstacles
        x, y = random.randint(1, width - 2), random.randint(1, height - 2)
        map[y][x] = random.randint(2, 4)

    return map

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 3, 0, 4, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 2, 4, 2, 2, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 3, 4, 0, 4, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = self.game.levels.map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, tile in enumerate(row):
                if tile:
                    self.world_map[(i, j)] = tile
                    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]