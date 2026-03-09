import pygame

from root.utils import update_sprt
from combat.profile import CombatProfile
from combat.combat_history import CombatHistory

# Create the real entity thats read in game

class Characters:
    def __init__(self, member):
        self.origin    = member
        self.codename  = member.codename
        self.on_screen = member.size
        self.position  = None
        self.chid      = 0
        
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'
        self.image = member.inner_galery['fighting']['idle']
        self.rect  = self.image.get_rect()
        
        self.items   = member.basic_items
        self.skills  = member.basic_skills
        self.passive = member.passive
        
        self.profile = CombatProfile(self)
        self.history = CombatHistory(self)
        self.clevel  = 1
        self.c_exp   = 0
        self.t_exp   = 0

    def level_up(self):
        from core.level import levels

        if self.c_exp >= levels[self.clevel]: # level up, apply current exp to total exp, reset current exp
            self.clevel += 1
            self.t_exp += self.c_exp
            self.c_exp = 0

    def update(self):
        update_sprt(self)
