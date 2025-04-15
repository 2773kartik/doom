import pygame as pg

class Sound():
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.spas12_fire = pg.mixer.Sound(self.path + 'SPASFIRE.ogg')