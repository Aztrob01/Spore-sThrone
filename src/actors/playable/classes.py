import pygame
import random
from core.passive_list import passive_list
from core.skill_engines import SkillEngine
from core.skill_list import skill_list
from root.utils import image_load
from root.settings import *

# -------------------------------------------
# C

class cvl:
    def __init__(self):
        self.mc       = 'DUELIST'
        self.codename = 'Cavaliere'
        self.name     = 'Claire Lemoine'

        self.size = SPRITE_S_N # ! Correction is needed
        self.inner_galery         = {
            'exploring':  image_load('./assets/image/classes/cvl/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/classes/cvl/idle.png'),
                'hitted':  image_load('./assets/image/classes/cvl/idle.png'),
                'selected': image_load('./assets/image/classes/cvl/idle.png'),
                'acting':   image_load('./assets/image/classes/cvl/idle.png'),
            },
            'defeated':  image_load('./assets/image/classes/cvl/idle.png'),
        }

        self.basic_stats   = {
            'hp': 100,
            'str': 20, 
            'dex': 40,
            'knw': 10,
            'lky': 20,
            'res': 10,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [skill_list['Pierce'], None, None, None]
        self.attack        = None # ! skill engine do ataque basico do duelista
        self.passive       = passive_list['d01']

# -------------------------------------------
# D
class dwf:
    def __init__(self):
        self.mc = 'WARRIOR'
        self.codename = 'Dwarf'
        self.name     = 'Kylian Johansson'

        self.size = SPRITE_S_N # square, low scale
        self.inner_galery         = {
            'exploring':  image_load('./assets/image/classes/dwf/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/classes/dwf/idle.png'),
                'hitted':  image_load('./assets/image/classes/dwf/idle.png'),
                'selected': image_load('./assets/image/classes/dwf/idle.png'),
                'acting':   image_load('./assets/image/classes/dwf/idle.png'),
            },
            'defeated':  image_load('./assets/image/classes/dwf/idle.png'),
        }
        self.basic_stats  = {
            'hp': 125,
            'str': 40, 
            'dex': 10,
            'knw': 0,
            'lky': 0,
            'res': 30,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [skill_list['Encourage'], None, None, None]
        
        self.attack  = None # ! skill engine do ataque basico do guerreiro
        self.passive = passive_list['w01']

# -------------------------------------------
# W

class wzr:
    def __init__(self):
        self.mc = 'MAGE'
        self.codename = 'Wizard'

        self.size = SPRITE_S_N # ! Correction is needed
        self.inner_galery         = {
            'exploring':  image_load('./assets/image/classes/wzr/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/classes/wzr/idle.png'),
                'hitted':  image_load('./assets/image/classes/wzr/idle.png'),
                'selected': image_load('./assets/image/classes/wzr/idle.png'),
                'acting':  image_load('./assets/image/classes/wzr/idle.png'),
            },
            'defeated':  image_load('./assets/image/classes/wzr/idle.png'),
        }

        self.basic_stats   = {
            'hp': 70,
            'str': 20, 
            'dex': 30,
            'knw': 30,
            'lky': 10,
            'res': 10,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [skill_list['Encourage'], None, None, None]
        self.attack        = None # ! skill engine do ataque basico do mago
        self.passive       = passive_list['m01']
