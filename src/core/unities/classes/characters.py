import pygame

from root.utils import update_sprite
from core.manager_sprite import AnimaSprite
from core.combat.profile import ProfileData

# Create the real entity thats read in game

class Characters:
    def __init__(self, user):
        self.job = user
        self.cid = 0
        self.profile = ProfileData(self)
        
        self.state   = ['fighting', 'idle']
        self.sprite  = AnimaSprite(self)
        self.rect    = None


