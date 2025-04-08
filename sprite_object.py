import pygame as pg
from settings import *
import os
from collections import deque

class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/fountain.png', 
                 pos=(1.5, 7.5), scale=0.6, shift=0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert()
        self.image.set_colorkey((0, 255, 255))
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_height = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift
    
    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        
        image = pg.transform.scale(self.image, (proj_width, proj_height))
        
        self.sprite_half_height = proj_height // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_height, HALF_HEIGHT - proj_height // 2 + height_shift
        
        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))
        
    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx , self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE
        
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()
        
    def update(self):
        self.get_sprite()
        
    
class AnimatedSprite(SpriteObject):
    def __init__(self, game, path='resources/sprites/animated_sprites/torch4/0.png',
                 pos=(1.5, 6.5), scale=0.7, shift=0.15, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False
        
    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)
        
    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]
        
    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_trigger = True
            self.animation_time_prev = time_now
        
    def get_images(self, path):
        images = deque()
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                img = pg.image.load(path+'/'+file).convert()
                img.set_colorkey((0,255,255))
                images.append(img)
        return images