import pygame, random

from core.manager_sprite import AnimaSprite
from core.combat.main_profile import ProfileData

class Entities:
    def __init__(self, entity):
        self.job        = entity
        self.codename   = entity.data['codename']
        


        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1

        self.profile = ProfileData(self)
        self.combat_profile = None
        
        self.state   = ['fighting', 'idle']
        self.sprite  = AnimaSprite(self)
        self.rect    = None
   

    def update(self):
        pass
        
        