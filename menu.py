import pygame as pg
from settings import *
import sys

class Menu:
    def __init__(self, game):
        self.game = game
        self.state = 0
        self.blood_screen = self.get_texture('resources/textures/DOOMBG.jpg', RES)
        self.logo = self.get_img('resources/sprites/static_sprites/DOOM.png')
        self.new_game = self.get_img('resources/sprites/static_sprites/NEWGAME.png')
        self.quit_game = self.get_img('resources/sprites/static_sprites/QUITGAME.png')
        self.sure = self.get_img('resources/sprites/static_sprites/SURE.png')
        self.pause = self.get_img('resources/sprites/static_sprites/PAUSE.png')
        self.accept = self.get_img('resources/sprites/static_sprites/ACCEPT.png')
        self.cancel = self.get_img('resources/sprites/static_sprites/CANCEL.png')
        self.which = self.get_img('resources/sprites/static_sprites/WHICH.png')
        self.l1 = self.get_img('resources/sprites/static_sprites/L1.png')
        self.l2 = self.get_img('resources/sprites/static_sprites/L2.png')
        self.l3 = self.get_img('resources/sprites/static_sprites/L3.png')
        self.play_sound = True
        self.game.sound.doom_music.play(-1)
        
    def get_img(self, path):
        img = pg.image.load(path).convert()
        img.set_colorkey((0, 255, 255))
        return pg.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
     
    def check_event(self):
        for ev in pg.event.get():
            if ev.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                print(mouse)
                if self.state == -1:
                    if HALF_WIDTH - self.accept.get_width()//2 < mouse[0] < HALF_WIDTH + self.accept.get_width()//2 and \
                       HEIGHT // 2 < mouse[1] < HEIGHT // 2 + self.accept.get_height():
                        pg.quit()
                        sys.exit()
                    elif HALF_WIDTH - self.cancel.get_width()//2 < mouse[0] < HALF_WIDTH + self.cancel.get_width()//2 and \
                         HEIGHT // 2 + 100 < mouse[1] < HEIGHT // 2 + 100 + self.cancel.get_height():
                        self.state = 0
                elif self.state == 0:
                    if HALF_WIDTH - self.new_game.get_width()//2 < mouse[0] < HALF_WIDTH + self.new_game.get_width()//2 and \
                       HEIGHT // 2 < mouse[1] < HEIGHT // 2 + self.new_game.get_height():
                        self.state = 1
                    elif HALF_WIDTH - self.quit_game.get_width()//2 < mouse[0] < HALF_WIDTH + self.quit_game.get_width()//2 and \
                         HEIGHT // 2 + 100 < mouse[1] < HEIGHT // 2 + 100 + self.quit_game.get_height():
                        self.state = -1
                elif self.state == 1:
                    if HALF_WIDTH - self.l1.get_width()//2 < mouse[0] < HALF_WIDTH + self.l1.get_width()//2 and \
                       HEIGHT // 2 < mouse[1] < HEIGHT // 2 + self.l1.get_height():
                        self.game.new_game(1)
                        self.game.sound.doom_music.stop()
                        self.game.menu_state = False
                    elif HALF_WIDTH - self.l2.get_width()//2 < mouse[0] < HALF_WIDTH + self.l2.get_width()//2 and \
                         HEIGHT // 2 + 100 < mouse[1] < HEIGHT // 2 + 100 + self.l2.get_height():
                        self.game.new_game(2)
                        self.game.menu_state = False
                    elif HALF_WIDTH - self.l3.get_width()//2 < mouse[0] < HALF_WIDTH + self.l3.get_width()//2 and \
                         HEIGHT // 2 + 200 < mouse[1] < HEIGHT // 2 + 200 + self.l3.get_height():
                        self.game.new_game(3)
                        self.game.menu_state = False
           
    def draw(self):
        if self.state == -1:
            self.game.screen.blit(self.blood_screen, (0, 0))
            self.game.screen.blit(self.sure, (HALF_WIDTH - self.sure.get_width()//2, HEIGHT // 4))
            self.game.screen.blit(self.accept, (HALF_WIDTH - self.accept.get_width()//2, HEIGHT // 2))
            self.game.screen.blit(self.cancel, (HALF_WIDTH - self.cancel.get_width()//2, HEIGHT // 2 + 100))
        if self.state == 0:
            self.game.screen.blit(self.blood_screen, (0, 0))
            self.game.screen.blit(self.logo, (HALF_WIDTH - self.logo.get_width()//2, HEIGHT // 4))
            self.game.screen.blit(self.new_game, (HALF_WIDTH - self.new_game.get_width()//2, HEIGHT // 2))
            self.game.screen.blit(self.quit_game, (HALF_WIDTH - self.quit_game.get_width()//2, HEIGHT // 2 + 100))
        if self.state == 1:
            self.game.screen.blit(self.blood_screen, (0, 0))
            self.game.screen.blit(self.which, (HALF_WIDTH - self.which.get_width()//2, HEIGHT // 4))
            self.game.screen.blit(self.l1, (HALF_WIDTH - self.l1.get_width()//2, HEIGHT // 2))
            self.game.screen.blit(self.l2, (HALF_WIDTH - self.l2.get_width()//2, HEIGHT // 2 + 100))
            self.game.screen.blit(self.l3, (HALF_WIDTH - self.l3.get_width()//2, HEIGHT // 2 + 200))
            
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)