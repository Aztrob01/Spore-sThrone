import pygame, random

from core.manager_sprite import AnimaSprite
from core.combat.profile import ProfileData

class Entities:
    def __init__(self, entity):
        self.job        = entity
        self.codename   = entity.data['info']['codename']


        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1

        self.profile = ProfileData(self)
        
        self.state   = ['fighting', 'idle']
        self.sprite  = AnimaSprite(self)
        self.rect    = None
   

    def update(self):
        pass
        
        