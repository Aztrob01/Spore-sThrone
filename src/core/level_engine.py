import pygame, random

from root.settings       import *
from root.utils import image_load
from core.level import *
from core.player_core  import PlayerCore
from actors.entities.entities   import Entities
from core.combat.combat_engine  import CombatEngine
from actors.entities.enemy import *


class LvlDataHandler:
    def __init__(self, data):
        self.levelnum = data['lvl']
        self.levelname = data['lvl_name']
        self.battleground = pygame.image.load(data['battleground'])
        self.battleground = pygame.transform.scale(self.battleground, (WIDTH, HEIGHT))
        
        self.entities  = data['entities_list']
        self.arealevel = data['area_level']

    def entities_randomize(self, n):
        import random
        from actors.entities.entities import Entities
        
        w = self.entities
        x = []
        
        for r in range(0, n):
            x.append(Entities(random.choice(w)()))
            x[-1].mlvl = random.randint(self.arealevel[0], self.arealevel[1])
        return x

class LevelEngine:
    def __init__(self, eventtoken):
        self.display = pygame.display.get_surface()
        self.player  = PlayerCore()
        self.token   = eventtoken
        
        self.data = {
            'lvl': 2,
            'lvl_name': 'Training Area',
            'area_level': [1, 5],
            'battleground': './assets/image/battlegrounds/sideviewerII.png',
            'entities_list': [gob, dmy] 
        }
        self.level   = LvlDataHandler(self.data)

        self.explore = None #! Correct Later
        self.combat  = CombatEngine(self.level, self.player, self.token)
        self.state   = 'fight'

        

    def play(self):
        if self.state == 'fight':
            self.combat.start()
        elif self.state == 'explore':
            pass