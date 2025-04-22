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
        self.spas12_fire.set_volume(0.15)
        self.spas12_change.set_volume(0.15)
        self.spas12_clic.set_volume(0.15)
        self.spas12_reload.set_volume(0.15)
        self.doom_music = pg.mixer.Sound(self.path + 'DOOM.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')