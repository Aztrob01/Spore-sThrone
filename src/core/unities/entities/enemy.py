import random, pygame

# -------------------------------------------
# D

class dmy:
    def __init__(self):
        self.data = {
            'class': { 'main': 'OBJECT' },
            'info': { 'name': 'Training Dummy', 'codename': 'Dummy' },
            'stats': { 'hp': 100, 'str': 0, 'dex': 0, 'knw': 0, 'lky': 0, 'res': 0 },
            'brain': { 'agr': 0, 'tac': 0, 'def': 0},
            'dimensions': 0.1, }
        
        self.madress = './src/assets/image/entities/dmy/'
        self.state_exceptions = { }

# -------------------------------------------
# G

class gob:
    def __init__(self):
        self.data = {
            'class': { 'main': 'MONSTER' },
            'info': { 'name': 'Mourzel Goblin', 'codename': 'Goblin' },
            'stats': { 'hp': 100, 'str': 20, 'dex': 30, 'knw': 10, 'lky': 0, 'res': 0 },
            'brain': { 'agr': 3, 'tac': 6, 'def': 1},
            'dimensions': 0.1, }
        
        self.madress = './src/assets/image/entities/dmy/'
        self.state_exceptions = { }