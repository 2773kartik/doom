from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        
        #sprite map
        for item in self.game.levels.static:
            add_sprite(SpriteObject(game, path=item[0], pos=item[1], scale=item[2],
                         shift=item[3], colorkey=item[5], alpha=item[4]))
        
        for item in self.game.levels.animated:
            add_sprite(AnimatedSprite(game, path=item[0], pos=item[1], scale=item[2],
                         shift=item[3], colorkey=item[5], alpha=item[4]))
        
        #npc map
        for item in self.game.levels.npc:
            add_npc(NPC(game, path=item[0], pos=item[1]))
        
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        
    def add_npc(self, npc):
        self.npc_list.append(npc)
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)