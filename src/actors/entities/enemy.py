import random, pygame
from core.passive_list import passive_list
from core.skill_engines import SkillEngine
from core.skill_list import skill_list
from root.settings import *
from root.utils import image_load

# -------------------------------------------
# D

class dmy:
    def __init__(self):
        self.main_class = 'Dummy'
        self.codename   = 'Dummy'

        self.size = SPRITE_S_N
        self.inner_galery = {
            'exploring': image_load('./assets/image/entities/dmy/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/entities/dmy/idle.png'),
                'hitted': image_load('./assets/image/entities/dmy/idle.png'),
                'selected': image_load('./assets/image/entities/dmy/idle.png'),
                'acting': image_load('./assets/image/entities/dmy/idle.png'),
            },
            'defeated': image_load('./assets/image/entities/dmy/idle.png')
        }
        self.brain = {
            'agr': 0, # aggressivenes
            'dex': 0, # dexterity as teamplay
            'def': 0, # defense as protection
        }
        self.basic_stats  = {
            'hp': 100,
            'str': 0,
            'dex': 0,
            'knw': 0,
            'lky': 0,
            'res': 0,
        }
        
        self.basic_skills = None
        self.passive      = None
        self.attack       = None #! skill engine do ataque basico do dummy

# -------------------------------------------
# G

class gob:
    def __init__(self):
        self.main_class = 'Monster'
        self.codename   = 'Goblin'

        self.size = SPRITE_S_S
        self.inner_galery = {
            'exploring': image_load('./assets/image/entities/gob/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/entities/gob/idle.png'),
                'hitted': image_load('./assets/image/entities/gob/idle.png'),
                'selected': image_load('./assets/image/entities/gob/idle.png'),
                'acting': image_load('./assets/image/entities/gob/idle.png'),
            },
            'defeated': image_load('./assets/image/entities/gob/idle.png')
        }
        self.brain = {
            'agr': 5, # aggressivenes
            'dex': 8, # dexterity as teamplay
            'def': 3, # defense as protection
        }
        self.basic_stats  = {
            'hp': 100,
            'str': 20,
            'dex': 30,
            'knw': 10,
            'lky': 0,
            'res': 0,
        }
        
        self.basic_skills = [skill_list['Pierce'], skill_list['Encourage']]
        self.passive      = None 
        self.attack       = None #! skill engine do ataque basico do goblin