import random, pygame

# -------------------------------------------
# D

class dmy:
    def __init__(self):
        self.data = {
            'name': 'Dummy',
            'type': 'Object',
            'codename': 'Dummy',
            
            'stats': { 'hp': 100, 'str': 0, 'dex': 0, 'knw': 0, 'lky': 0, 'res': 0 },
            'brain': { 'agr': 0, 'tac': 0, 'def': 0},
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
            'adress': './src/assets/image/entities/dmy/',
            'dimensions': 0.12,
        }

        self.name = self.data['name']

# -------------------------------------------
# G

class gob:
    def __init__(self):
        self.data = {
            'name': 'Goblin',
            'type': 'Monster',
            'codename': 'Goblin',
            
            'stats': { 'hp': 100, 'str': 20, 'dex': 30, 'knw': 10, 'lky': 32, 'res': 0 },
            'brain': { 'agr': 3, 'tac': 6, 'def': 1},
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
            'adress': './src/assets/image/entities/gob/',
            'dimensions': 0.12,
        }

        self.name = self.data['name']