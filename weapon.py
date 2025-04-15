from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapons/SPAS12/fire/0.png',
                 click_path='resources/sprites/weapons/SPAS12/change/0.png',
                 reload_path='resources/sprites/weapons/SPAS12/reload/0.png',
                 scale=2, animation_time=90, alpha = True, ammo=2):
        super().__init__(game, path, scale=scale, animation_time=animation_time, alpha=alpha)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images]
        )
        self.image = self.images[0]
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.change = False
        self.reloading = False
        self.click_path = click_path.rsplit('/', 1)[0]
        self.click_images = self.get_images(self.click_path)
        self.click_images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.click_images]
        )
        self.reload_path = reload_path.rsplit('/', 1)[0]
        self.reload_images = self.get_images(self.reload_path)
        self.reload_images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.reload_images]
        )
        self.num_images = len(self.images)
        self.num_click_images = len(self.click_images)
        self.num_reload_images = len(self.reload_images)
        self.frame_counter = 0
        self.damage = 50
        self.click = False
        self.ammo = ammo
        self.ammo_counter = 0
        
    def animate_shot(self):
        if self.click:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter >= self.num_images:
                    self.frame_counter = 0
                    self.click = False
                    if self.ammo_counter >= self.ammo:
                        self.reloading = True
                        self.ammo_counter = 0
                        self.game.sound.spas12_clic.play()
                    else:
                        self.change = True
                        self.game.sound.spas12_change.play()
        if self.change:
            if self.animation_trigger:
                self.click_images.rotate(-1)
                self.image = self.click_images[0]
                self.frame_counter += 1
                if self.frame_counter >= self.num_click_images:
                    self.frame_counter = 0
                    self.change = False
                    self.ammo_counter += 1
        if self.reloading:
            if self.animation_trigger:
                self.reload_images.rotate(-1)
                self.image = self.reload_images[0]
                self.frame_counter += 1
                if self.frame_counter >= self.num_reload_images:
                    self.frame_counter = 0
                    
                    self.reloading = False
                    self.game.sound.spas12_reload.play()    
        
    def draw(self):
        self.game.screen.blit(self.image, self.weapon_pos)
        
    def update(self):
        self.check_animation_time()
        self.animate_shot()