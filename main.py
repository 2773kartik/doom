import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from object_handler import *
from weapon import *
from sound import *
from pathfinder import *
from levels import *
from menu import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_event = pg.USEREVENT + 0
        self.global_trigger = False
        self.menu_state = True
        pg.time.set_timer(self.global_event, 40)
        self.sound = Sound(self)
        self.menu = Menu(self)
    
    def new_game(self, level):
        self.levels = Levels(self, level)
        self.object_renderer = ObjectRenderer(self)
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.pathfinder = Pathfinding(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
        
    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.player.draw()
        # self.map.draw()
    
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.menu.state = -1
                self.menu_state = True
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
                
    def run(self):
        while True:
            if not self.menu_state:
                self.check_events()
                self.update()
                self.draw()
            else:
                self.menu.check_event()
                pg.display.flip()
                self.menu.draw()                
            
if __name__ == "__main__":
    game = Game()
    game.run()