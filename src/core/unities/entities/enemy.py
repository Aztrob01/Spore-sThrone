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
            'dimensions': 0.12, }
        
        self.madress = './src/assets/image/entities/dmy/'
        self.shadowtype = None
        self.state_exceptions = { }

        def_sk = None

# -------------------------------------------
# G

class gob:
    def __init__(self):
        self.data = {
            'class': { 'main': 'MONSTER' },
            'info': { 'name': 'Mourzel Goblin', 'codename': 'Goblin' },
            'stats': { 'hp': 100, 'str': 20, 'dex': 30, 'knw': 10, 'lky': 0, 'res': 0 },
            'brain': { 'agr': 3, 'tac': 6, 'def': 1},
            'dimensions': 0.12, }
        
        self.madress = './src/assets/image/entities/gob/'
        self.shadowtype = None
        self.state_exceptions = { }