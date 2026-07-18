class Profiles:
    def __init__(self):
        self.data = {
            
            'origin': None, 'status': [], 'level': 1,
            'skills': [], 'passives': [],
            
            'static': { 'raw': { }, 'rec': { }, 'stats': { } },
            
            'multipliers': { }, 'bonus': { },

            'recipe': {  'attr': { }, 'stats': { } },

            'interactive': { 'current': { 'hp': 0, 'mp': 0, 'shield': 0 } }
        }

    def load_origin(self, origin):
        self.data['origin'] = origin

    def set_static(self):
        if self.data['origin'] is None:
            print('No origin is loaded for this condition. RawAttr ended')
            exit(-1)

        self.data['static']['raw'] = self.data['origin'].data['rawAttr']
        self.data['static']['rec'] = { 'vit': 0, 'str': 0, 'dex': 0, 'knw': 0, 'res': 0, 'lky': 0 }
        self.data['static']['stats'] = {

            'reg':  { 'hp': 0, 'mp': 0 },
            'heal': { 'inc': 0, 'out': 0 },
            'shield': { 'inc': 0, 'cur': 0, 'out': 0 },
            'cr': { 'rate': 0.05, 'dmg': 0.7 },

            'cdt': 1, 'damp': 1, 'drec': 1, 'lifesteal': 0 } # higher cdt means longer cooldown
        print('RawAttr Loaded.')

    def reset_multipliers(self):
        self.data['multipliers'] = {
            
            'attr': 
                { 
                    'vit': 1,
                    'str': 1,
                    'dex': 1,
                    'knw': 1,
                    'res': 1,
                    'lky': 1
                
                 },
            'stats': 
                { 

                    'hp': { 'max': 1, 'ori': 1 }, 'mp': { 'max': 1, 'ori': 1 }, 'reg': { 'hp': 1, 'mp': 1 },
                
                    'heal': { 'inc': 1, 'out': 1 },
                    'shield': { 'inc': 1, 'cur': 1, 'out': 1 },
                    'cr': { 'rate': 1, 'dmg': 1 },

                    'cdt': 1, 
                    'damp': 1,
                    'drec': 1,
                    'lifesteal': 1,
                    'def': 1, 

                 },
            
        }
        self.data['bonus'] = { 
            'attr': 
                { 
                    'vit': 0,
                    'str': 0,
                    'dex': 0,
                    'knw': 0,
                    'res': 0,
                    'lky': 0
                
                 },
            'stats': 
                { 

                    'hp': { 'max': 0, 'ori': 0 }, 'mp': { 'max': 0, 'ori': 0 }, 'reg': { 'hp': 0, 'mp': 0 },
                
                    'heal': { 'inc': 0, 'out': 0 },
                    'shield': { 'inc': 0, 'cur': 0, 'out': 0 },
                    'cr': { 'rate': 0, 'dmg': 0 },

                    'cdt': 0, 
                    'damp': 0,
                    'drec': 0,
                    'lifesteal': 0,
                    'def': 0, 

                 },
            
        }

    def set_dynamicAttr(self):
        mul = self.data['multipliers']
        bonus = self.data['bonus']
        lvl = self.data['level']
        atr, rec = self.data['static']['raw'], self.data['static']['rec']

        self.data['recipe']['attr'] = {
            
            'vit': ((atr['vit'] + rec['vit']) * mul['attr']['vit']) + bonus['attr']['vit'],
            'str': ((atr['str'] + rec['str']) * mul['attr']['str']) + bonus['attr']['str'],
            'dex': ((atr['dex'] + rec['dex']) * mul['attr']['dex']) + bonus['attr']['dex'],
            'knw': ((atr['knw'] + rec['knw']) * mul['attr']['knw']) + bonus['attr']['knw'],
            'res': ((atr['res'] + rec['res']) * mul['attr']['res']) + bonus['attr']['res'],
            'lky': ((atr['lky'] + rec['lky']) * mul['attr']['lky']) + bonus['attr']['lky'],
        
        }

    def set_dynamicRecipe(self):
        atr, mul, bonus = self.data['recipe']['attr'], self.data['multipliers'], self.data['bonus']
        sts = self.data['static']['stats']

        self.data['recipe']['stats'] = {

            'hp': 
                { 
                    'max': (atr['vit'] + bonus['stats']['hp']['max']) * mul['stats']['hp']['max'], 
                    'ori': (atr['vit'] + bonus['stats']['hp']['ori']) * mul['stats']['hp']['ori'],
                }, 
            'mp': 
                {
                    'max': (atr['knw'] + bonus['stats']['mp']['max']) * mul['stats']['mp']['max'],
                    'ori': (atr['knw'] + bonus['stats']['mp']['ori']) * mul['stats']['mp']['ori'] 
                },
            'reg': 
                { 
                    'hp': (sts['reg']['hp'] * mul['stats']['reg']['hp']) + bonus['stats']['reg']['hp'],
                    'mp': (sts['reg']['mp'] * mul['stats']['reg']['mp']) + bonus['stats']['reg']['mp']
                },
            'heal': 
                { 
                    'inc': (sts['heal']['inc'] * mul['stats']['heal']['inc']) + bonus['stats']['heal']['inc'],
                    'out': (sts['heal']['out'] * mul['stats']['heal']['out']) + bonus['stats']['heal']['out']
                },
            'shield': 
                {
                    'inc': (sts['shield']['inc'] * mul['stats']['shield']['inc']) + bonus['stats']['shield']['inc'],
                    'out': (sts['shield']['out'] * mul['stats']['shield']['out']) + bonus['stats']['shield']['out']
                },
                'cr': 
                {
                    'rate': (sts['cr']['rate'] * mul['stats']['cr']['rate']) + bonus['stats']['cr']['rate'],
                    'dmg': (sts['cr']['dmg'] * mul['stats']['cr']['dmg']) + bonus['stats']['cr']['dmg']
                },

            'cdt': (sts['cdt'] / mul['stats']['cdt']) - bonus['stats']['cdt'], # as cdt increasement means longer cooldown, we invert the equation 
            'damp': (sts['damp'] * mul['stats']['damp']) + bonus['stats']['damp'],
            'drec': (sts['drec'] * mul['stats']['drec']) + bonus['stats']['drec'],
            'lifesteal': (sts['lifesteal'] * mul['stats']['lifesteal']) + bonus['stats']['lifesteal'],
            'def': ((atr['res'] / 4) * mul['stats']['def']) + bonus['stats']['def'],

        }

    def say_attr(self): #! Just for Debugging purposes
        bonus = self.data['bonus']
        cur = self.data['interactive']['current']
        sts = self.data['recipe']['stats']
        atr =  self.data['recipe']['attr']

        print(f'\nHP: {cur['hp']}/{sts['hp']['max']} of {sts['hp']['ori']} | (+{sts['reg']['hp']} per round)' )
        print(f'MP: {cur['mp']}/{sts['mp']['max']} of {sts['mp']['ori']} | (+{sts['reg']['mp']} per round)')
        print(f'DETAILS ----------------------')
        print(f'Critical Rate: {sts['cr']['rate'] * 100}% | Critical Damage: {sts['cr']['dmg'] * 100}%')
        print(f'Damage Amplification: {sts['damp'] * 100}% | Damage Reduction: {sts['drec'] * 100}%')
        print(f'Life Steal: {sts['lifesteal'] * 100}%')
        print(f'Cooldown Time: {sts['cdt']}x')
        print(f'Defense: {sts['def']} points')
        print(f'ATTRIBUTES ----------------------')
        print(f'Vitality: {atr['vit']} (+{bonus['attr']['vit']})\nStrenght: {atr['str']} (+{bonus['attr']['str']})')
        print(f'Dexterity: {atr['dex']} (+{bonus['attr']['dex']})\nKnowledge: {atr['knw']} (+{bonus['attr']['knw']})')
        print(f'Resilience: {atr['res']} (+{bonus['attr']['res']})\nLucky: {atr['lky']} (+{bonus['attr']['lky']})\n')


