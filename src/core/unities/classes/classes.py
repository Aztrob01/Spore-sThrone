import pygame
import random

# -------------------------------------------
# C

class cvl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'DUELIST' }, 
            'info':  { 'name': 'Claire Lemoine', 'codename': 'Cavaliere' },
            'stats': { 'hp': 100, 'str': 20, 'dex': 40, 'knw': 10, 'lky': 20, 'res': 10 },
            'dimensions': 0.12,
        }
        
        self.madress = './src/assets/image/classes/cvl/'
        self.shadowtype = None
        self.state_exceptions = { }

class dpl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'TANK' }, 
            'info':  { 'name': 'Friedrich Knikovw', 'codename': 'Doppelsoldier' },
            'stats': { 'hp': 130, 'str': 40, 'dex': 10, 'knw': 10, 'lky': 5, 'res': 35 },
            'dimensions': 0.12,
        }
        
        self.madress = './src/assets/image/classes/cvl/'
        self.shadowtype = None
        self.state_exceptions = { }

class alc:
    def __init__(self):
        self.data = {
            'class': { 'main': 'MAGE' }, 
            'info':  { 'name': 'Lizze Osborn', 'codename': 'Alchemist' },
            'stats': { 'hp': 80, 'str': 10, 'dex': 30, 'knw': 40, 'lky': 10, 'res': 10 },
            'dimensions': 0.12,
        }
        
        self.madress = './src/assets/image/classes/alc/'
        self.shadowtype = None
        self.state_exceptions = { }
    