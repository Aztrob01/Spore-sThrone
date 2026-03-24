import pygame, random

from combat.combat_buffer import CombatBuffer
from root.utils import update_sprt

class Entities:
    def __init__(self, entity):
        self.origin     = entity
        self.codename   = entity.codename
        self.on_screen  = entity.size
        self.image = entity.inner_galery['fighting']['idle']
        self.rect  = self.image.get_rect()

        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1
        self.buffer     = None
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'
   

    def update(self):
        update_sprt(self)
        
        