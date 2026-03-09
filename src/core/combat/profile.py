
# Cares ONLY ABOUT THE FREAKING COMBAT PROFILE
# things like COMBAT MULTIPLIERS and STATS
# * DO NOT ALLOW IT MAKE ACTIONS (SRP****)


class CombatProfile:
    def __init__(self, user):
        self.user   = user
        
        self.atk     = user.origin.attack
        self.skills  = user.skills
        self.passive = user.passive
        
        self.action_pool = [self.atk] # actions list to append in perfils

        self.INPUT_STATS = {
            'hp': 0,
            'str': 0,
            'dex': 0,
            'knw': 0,
            'lky': 0,
            'res': 0
        }
        self.BRUTE_STATS = {
            'hp': self.INPUT_STATS['hp'] + user.origin.basic_stats['hp'],
            'str': self.INPUT_STATS['str'] + user.origin.basic_stats['str'],
            'dex': self.INPUT_STATS['dex'] + user.origin.basic_stats['dex'],
            'knw': self.INPUT_STATS['knw'] + user.origin.basic_stats['knw'],
            'lky': self.INPUT_STATS['lky'] + user.origin.basic_stats['lky'],
            'res': self.INPUT_STATS['res'] + user.origin.basic_stats['res']
        }
        
        self.MAXIMUM_HP = self.BRUTE_STATS['hp']
        self.CURRENT_HP = self.MAXIMUM_HP
        self.STRENGHT   = self.BRUTE_STATS['str'] 
        
        self.DEXTERITY  = self.BRUTE_STATS['dex']
        self.LUCKY      = self.BRUTE_STATS['lky'] 
        self.CRITICAL_CH  = (5 + (self.BRUTE_STATS['lky'] / 10)) / 100 # critical chance evolves with LKY
        self.CRITICAL_DMG = (150 + (self.BRUTE_STATS['dex'] / 10)) / 100 # critical damage evolves with DEX
        self.OUTPUT_DAMAGE_MULTIPLIER = 1 # damage output. Default value is 1

        self.INPUT_DAMAGE_MULTIPLIER = 1
        self.RESISTANCE = self.BRUTE_STATS['res'] / 2 # reduce the incoming damage by half of the RES

        self.KNOWLEDGE  = self.BRUTE_STATS['knw']
        self.MAGICAL_DAMAGE_MULTIPLIER = (100 + (self.KNOWLEDGE / 10)) / 100 # multiplies MAGICAL DAMAGE

    def reset_brute(self):
        self.BRUTE_STATS = {
            'hp': self.INPUT_STATS['hp'] + self.user.origin.basic_stats['hp'],
            'str': self.INPUT_STATS['str'] + self.user.origin.basic_stats['str'],
            'dex': self.INPUT_STATS['dex'] + self.user.origin.basic_stats['dex'],
            'knw': self.INPUT_STATS['knw'] + self.user.origin.basic_stats['knw'],
            'lky': self.INPUT_STATS['lky'] + self.user.origin.basic_stats['lky'],
            'res': self.INPUT_STATS['res'] + self.user.origin.basic_stats['res']
    }
        
    def reset_entries(self):
        self.MAXIMUM_HP = self.BRUTE_STATS['hp']
        self.CURRENT_HP = self.MAXIMUM_HP
        self.STRENGHT   = self.BRUTE_STATS['str'] 
        
        self.DEXTERITY  = self.BRUTE_STATS['dex']
        self.LUCKY      = self.BRUTE_STATS['lky'] 
        self.CRITICAL_CH  = (5 + (self.BRUTE_STATS['lky'] / 10)) / 100
        self.CRITICAL_DMG = (150 + (self.BRUTE_STATS['dex'] / 10)) / 100
        self.OUTPUT_DAMAGE_MULTIPLIER = 1

        self.INPUT_DAMAGE_MULTIPLIER = 1
        self.RESISTANCE = self.BRUTE_STATS['res']

        self.KNOWLEDGE  = self.BRUTE_STATS['knw']
        self.MAGICAL_DAMAGE_MULTIPLIER = (100 + (self.KNOWLEDGE / 10)) / 100

    def pool_update(self):
        for nums, items in enumerate(self.skills):
            if self.skills[nums] != None:
                if items not in self.action_pool:
                    self.action_pool.append(items)

        if len(self.action_pool) > 5:
            for items in self.action_pool:
                print(items.name)
            raise ValueError('A lista de ações excedeu seu limite!')