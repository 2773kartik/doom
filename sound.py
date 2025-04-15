import pygame as pg

class Sound():
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.spas12_fire = pg.mixer.Sound(self.path + 'SPASFIRE.ogg')
        self.spas12_change = pg.mixer.Sound(self.path + 'SPASCOC2.ogg')
        self.spas12_clic = pg.mixer.Sound(self.path + 'SPASCLIC.ogg')
        self.spas12_reload = pg.mixer.Sound(self.path + 'SPASLOAD.ogg')