import pygame, random

from core.manager_sprite import AnimaSprite

class Entities:
    def __init__(self, entity):
        self.job        = entity
        self.codename   = entity.data['info']['codename']

        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1

        self.state  = ['fighting', 'idle']
        self.sprite = AnimaSprite(self)
        self.rect   = None
   

    def update(self):
        pass
        
        