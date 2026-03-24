import pygame
import random
from core.passive_list import passive_list
from core.skill_engines import SkillEngine
from core.skill_list import skill_list
from core.root.utils import image_load
from core.root.settings import *

# -------------------------------------------
# C

class cvl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'DUELIST', 'secondary': 'HIBRID' }, 
            'info':  { 'name': 'Claire Lemoine', 'codename': 'Cavaliere' },
            'stats': { 'hp': 100, 'str': 20, 'dex': 40, 'knw': 10, 'lky': 20, 'res': 10 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': COMMON_SPRITE_SIZE,
                'others': None,
            }
        }

class dpl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'TANK', 'secondary': 'DAMAGE' }, 
            'info':  { 'name': 'Friedrich Knikovw', 'codename': 'Doppelsoldier' },
            'stats': { 'hp': 130, 'str': 40, 'dex': 10, 'knw': 10, 'lky': 5, 'res': 35 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': COMMON_SPRITE_SIZE,
                'others': None,
            }
        }


class alc:
    def __init__(self):
        self.data = {
            'class': { 'main': 'MAGE', 'secondary': 'DAMAGE' }, 
            'info':  { 'name': 'Lizze Osborn', 'codename': 'Alchemist' },
            'stats': { 'hp': 80, 'str': 10, 'dex': 30, 'knw': 40, 'lky': 10, 'res': 10 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': COMMON_SPRITE_SIZE,
                'others': None,
            }
        }