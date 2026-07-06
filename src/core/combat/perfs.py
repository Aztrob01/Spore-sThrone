class Perfils:
    def __init__(self):
        self.data = {
            
            'origin': None, 'stats': [], 'level': 1,
            'skills': [], 'passives': [],

            'raw': { 'vit': 0, 'str': 0, 'dex': 0, 'knw': 0, 'res': 0, 'lky': 0 },
            'received': { 'vit': 0, 'str': 0, 'dex': 0, 'knw': 0, 'res': 0, 'lky': 0 },
            'multipliers': { 'attr': { }, 'composed': { }, 'extras': { }, },
            'bonus': { 'attr': { }, 'composed': { }, 'extras': { }, },

            'attr': { },
            'composed': { },
            'vals': { },
            'extras': { },

        }

    def load_origin(self, origin):
        self.data['origin'] = origin

    def load_rawAttr(self):
        if self.data['origin'] is None:
            print('No origin is loaded for this condition. RawAttr ended')
            exit(-1)

        self.data['raw'] = self.data['origin'].data['rawAttr']

    def load_received(self, points):
        for nums, vals in enumerate(self.data['received']):
            self.data['received'][vals] = points[nums]
            print(vals, 'recebe', points[nums], 'agora.')

    def set_mult(self):
        self.data['multipliers'] = {
            'attr': { 'vit': 1, 'str': 1, 'dex': 1, 'knw': 1, 'res': 1, 'lky': 1 },

            'composed': { 'hp': { 'max': 1, 'ori': 1, 'reg': 1 }, 'mp': { 'max': 1, 'ori': 1, 'reg': 1 } },
            'extras': { 'lf': 1, 'cr': { 'rate': 1, 'dmg': 1 }, 'cdr': 1, 'res': 1, 'dmg': 1 } 
        }

    def set_bonus(self):
        self.data['bonus'] = { 
            'attr': { 'vit': 0, 'str': 0, 'dex': 0, 'knw': 0, 'res': 0, 'lky': 0 },
            
            
            'extras': { 'lf': 0, 'cr': { 'rate': 0, 'dmg': 0 }, 'cdr': 0, 'res': 0, 'dmg': 0, 'mp_reg': 0, 'hp_reg': 0 },
            'composed': { 'hp': { 'max': 0, 'ori': 0, 'reg': 0 }, 'mp': { 'max': 0, 'ori': 0, 'reg': 0 } },
            
        }

    def set_attr(self):
        vit = self.data['raw']['vit']
        str = self.data['raw']['str']
        dex = self.data['raw']['dex']
        knw = self.data['raw']['knw']
        res = self.data['raw']['res']
        lky = self.data['raw']['lky']
        
        level = self.data['level']
        gained = self.data['received']

        multipliers = self.data['multipliers']['attr']
        bonus = self.data['bonus']['attr']

        self.data['attr'] = {
            'vit': ((vit + level + gained['vit']) * multipliers['vit']) + bonus['vit'],
            'str': ((str + level + gained['str']) * multipliers['str']) + bonus['str'],
            'dex': ((dex + level + gained['dex']) * multipliers['dex']) + bonus['dex'],
            'knw': ((knw + level + gained['knw']) * multipliers['knw']) + bonus['knw'],
            'res': ((res + level + gained['res']) * multipliers['res']) + bonus['res'],
            'lky': ((lky + level + gained['lky']) * multipliers['lky']) + bonus['lky'],
        }

    def set_composed(self):
        multiplier = self.data['multipliers']['composed']
        bonus = self.data['bonus']['composed']
        attr = self.data['attr']

        self.data['composed'] = {
            'hp': { 
                   'ori': (attr['vit'] * multiplier['hp']['ori']) + bonus['hp']['ori'],
                   'max': (attr['vit'] * multiplier['hp']['max']) + bonus['hp']['max'],
                   'reg': (1 * multiplier['hp']['reg']) + bonus['hp']['reg']},
            'mp': {
                  'ori': ((attr['knw'] / 3) * multiplier['mp']['ori']) + bonus['mp']['ori'],
                  'max': ((attr['knw'] / 3) * multiplier['mp']['max']) + bonus['mp']['max'],
                  'reg': (1 * multiplier['hp']['reg']) + bonus['mp']['reg']},
        }