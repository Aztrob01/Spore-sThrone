class Alc:
    def __init__(self):
        self.data = { 
            
            'type': 'playable',
            'name': None, 'family': None,
            'type': None, 'codename': None, 'affiliation': None,

            'rawAttr': { 'vit': 60, 'str': 10, 'dex': 30, 'knw': 40, 'lky': 10, 'res': 10 },
            'skilltree': { 'default': { }, 'acquirable': { } },

        }

class Cvl:
    def __init__(self):
        self.data = { 
            
            'type': 'playable',
            'name': None, 'family': None,
            'type': None, 'codename': 'Cavaliere', 'affiliation': None,

            'rawAttr': { 'vit': 70, 'str': 20, 'dex': 40, 'knw': 10, 'lky': 20, 'res': 10 },
            'skilltree': { 'default': { }, 'acquirable': { } },

        }

class Dpl:
    def __init__(self):
        self.data = { 

            'type': 'playable',
            'name': None, 'family': None,
            'type': None, 'codename': None, 'affiliation': None,

            'rawAttr': { 'hp': 130, 'str': 40, 'dex': 10, 'knw': 10, 'lky': 5, 'res': 35 },
            'skilltree': { 'default': { }, 'acquirable': { } },

        }