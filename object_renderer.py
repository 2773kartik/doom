import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture(self.game.levels.sky, res=(WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/FIREMAG1.png', RES)
        self.digit_size = 80
        self.digit_images = [self.get_texture(f'resources/textures/digit/{i}.png', res=(self.digit_size, self.digit_size)) for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_screen = self.get_texture('resources/textures/GAMEOVER.png', RES)
    
    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()
        
    def game_over(self):
        self.screen.blit(self.game_over_screen, (0, 0))
        
    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i*self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i+1)*self.digit_size, 0))
        
    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))
        
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH

        # Draw sky
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        # Draw floor base color
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

        # Create and draw reflection
        flipped_sky = pg.transform.flip(self.sky_image, True, True)
        flipped_sky.set_alpha(10)  # Make it partially transparent

        self.screen.blit(flipped_sky, (-self.sky_offset, HALF_HEIGHT))
        self.screen.blit(flipped_sky, (-self.sky_offset + WIDTH, HALF_HEIGHT))


    
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, texture, pos in list_objects:
            self.screen.blit(texture, pos)
    
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            i+1: self.get_texture(self.game.levels.wall[i]) for i in range(len(self.game.levels.wall))
        }