import pygame, random

import os
from game.core.cmb_eng import CombatEngine

class PlayerManager:
    def __init__(self):
        self.state = 'waiting...'

    def create(self): # create with OS PATH is working
        path = './src/game/users/save.json'
        if os.path.exists(path):
            import json
            # check if archive is not cleared
            # use try to handle exceptions on JSON and avoid corrupt the save

    def reset(self):
        pass

    def delete(self):
        pass

    def load(self):
        pass

    def save(self):
        pass

class LevelManager:
    def __init__(self, lvl_data):
        self.data = lvl_data

    def read(self, path):
        path = f'./src/game/world/{path}.json'

        if os.path.exists(path):
            pass
            
            



class LevelEngine:
    def __init__(self, eventtoken):
        self.display = pygame.display.get_surface()
        
        self.token   = eventtoken
        self.player  = None # static data
        self.level   = None # if game isnt in the worldphase, the engine needs to update level
        
        self.explore = None # need to be completed
        self.combat  = CombatEngine(self.level, self.player, self.token)
        self.state   = 'fight'

        

    def play(self):
        if self.state == 'fight':
            self.combat.start()
        elif self.state == 'explore':
            pass