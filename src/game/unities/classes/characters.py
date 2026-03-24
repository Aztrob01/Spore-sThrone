import pygame

from core.root.utils import update_sprite
from core.combat.profile import ProfileData

# Create the real entity thats read in game

class Characters:
    def __init__(self, user):
        self.job = user
        self.profile = ProfileData(user) 

        self.state = ['fighting', 'idle']
        self.image = None
        self.rect  = None

    def update(self):
        update_sprite(self.state, self)

