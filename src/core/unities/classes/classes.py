import pygame
import random

# -------------------------------------------
# C

class cvl:
    def __init__(self):
        self.data = {
            'name': 'Claire',
            'family': "D'lune",
            'type': 'Duelist',
            'codename': 'Cavaliere',
            'affiliation': None,
            
            'stats': { 'hp': 100, 'str': 20, 'dex': 40, 'knw': 10, 'lky': 20, 'res': 10 },
            'skills': {
                'passive': {
                    'main': None,
                    'family': None,
                },
                'active': {
                    'sk_0': None,
                    'sk_1': None,
                    'sk_2': None,
                    'sk_3': None,
                    'sk_ult': None,
                }
            },

            'shadow_type': None,
            'state_exceptions': None,
            'adress': './src/assets/image/classes/cvl/',
            'dimensions': 0.12,
        }
        
        self.name = self.data['name'] + ' ' + self.data['family']
    

class dpl:
    def __init__(self):
        self.data = {
            'name': 'Friedrich',
            'family': 'Knikovw',
            'type': 'Warrior',
            'codename': 'Doppelsoldier',
            'affiliation': 'Soldiers',
            
            'stats': { 'hp': 130, 'str': 40, 'dex': 10, 'knw': 10, 'lky': 5, 'res': 35 },
            'skills': {
                'passive': {
                    'main': None,
                    'family': None,
                },
                'active': {
                    'sk_0': None,
                    'sk_1': None,
                    'sk_2': None,
                    'sk_3': None,
                    'sk_ult': None,
                }
            },

            'shadow_type': None,
            'state_exceptions': None,
            'adress': './src/assets/image/classes/dpl/',
            'dimensions': 0.12,
        }
        
        self.name = self.data['name'] + ' ' + self.data['family']

class alc:
    def __init__(self):
        self.data = {
            'name': 'Lizz',
            'family': 'Orbourn',
            'type': 'Mage',
            'codename': 'Alchemist',
            'affiliation': 'Alchemists',
            
            'stats': { 'hp': 80, 'str': 10, 'dex': 30, 'knw': 40, 'lky': 10, 'res': 10 },
            'skills': {
                'passive': {
                    'main': None,
                    'family': None,
                },
                'active': {
                    'sk_0': None,
                    'sk_1': None,
                    'sk_2': None,
                    'sk_3': None,
                    'sk_ult': None,
                }
            },
            
            'shadow_type': None,
            'state_exceptions': None,
            'adress': './src/assets/image/classes/alc/',
            'dimensions': 0.12,
        }

        self.name = self.data['name'] + ' ' + self.data['family']



coco = cvl()
print(coco.name)