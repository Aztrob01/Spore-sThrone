class CombatProfileData:
    def __init__(self, user):
        self.user      = user
        self.user_data = user.job.data
        
        self.status    = {
            'passives': [user.job.data['skills']['passive']['main'], user.job.data['skills']['passive']['family']],
            'buffs':   [],
            'debuffs': [],
        }
        self.allies    = {}
        self.targets   = {}

        self.main_stats = user.profile.stats
        self.multipliers  = {
            'hp': {
                'original_hp_multiplier': 1, 'maximum_hp_multiplier': 1, 'extra_hp_multiplier': 1,
                'original_hp_bonus': 0, 'maximum_hp_bonus': 0, 'extra_hp_bonus': 0,
            },
            'mp': {
                'maximum_mp_multiplier': 1, 'recovery_mp_multiplier': 1,
                'maximum_mp_bonus': 0, 'recovery_mp_bonus': 0,
            },
            'damage': {
                'sk_damage_multiplier': 1, 'damage_multiplier': 1, 'cr_damage_multiplier': 1, 'cr_rate_multiplier': 1,
                'sk_damage_bonus': 0, 'damage_bonus': 0, 'cr_damage_bonus': 0, 'cr_rate_bonus': 0,
            },
            'resistance': {
                'sk_resistance_multiplier': 1, 'resistance_multiplier': 1, 'cr_resistance_multiplier': 1,
                'sk_resistance_bonus': 0, 'resistance_bonus': 0, 'cr_resistance_bonus': 0,
            },
            'healing': {
                'healing_multiplier': 1,
                'lifesteal_multiplier': 1,
                'healing_bonus': 0,
            },
        }
        self.static_stats = {
            'hp': { 
                'current': self.main_stats['hp']['current'],
                'extra': 0,
                  },
            'mp': {
                'current': self.main_stats['mp']['current'],
                'recover': (self.main_stats['mp']['recover'] * self.multipliers['mp']['recovery_mp_multiplier']) + self.multipliers['mp']['recovery_mp_bonus'],
            },
            'healing': {
                'lifesteal': 0,
            }
        }
        self.action_stats = {
            'hp': { 
                'original': (self.main_stats['hp']['original'] * self.multipliers['hp']['original_hp_multiplier']) + self.multipliers['hp']['original_hp_bonus'],
                'maximum': (self.main_stats['hp']['maximum'] * self.multipliers['hp']['maximum_hp_multiplier']) + self.multipliers['hp']['maximum_hp_bonus'],
                  },
            'mp': {
                'original': (self.main_stats['mp']['original'] * self.multipliers['mp']['maximum_mp_multiplier']) + self.multipliers['mp']['maximum_mp_bonus'],
                'maximum': (self.main_stats['mp']['maximum'] * self.multipliers['mp']['maximum_mp_multiplier']) + self.multipliers['mp']['maximum_mp_bonus'],
                'recover': (self.main_stats['mp']['recover'] * self.multipliers['mp']['recovery_mp_multiplier']) + self.multipliers['mp']['recovery_mp_bonus'],
            },
            'damage': {
                'cr_rate': (self.main_stats['damage']['cr_rate'] * self.multipliers['damage']['cr_rate_multiplier']) + (self.multipliers['damage']['cr_rate_bonus'] / 100),
                'cr_damage': (self.main_stats['damage']['cr_damage'] * self.multipliers['damage']['cr_damage_multiplier']),
            },
            'resistance': {
                'resistance': (self.main_stats['resistance']['resistance'] * self.multipliers['resistance']['resistance_multiplier']),
            },
            'healing': {
                'healing': (self.main_stats['healing']['healing_base'] * self.multipliers['healing']['healing_multiplier']),
                'lifesteal': (self.main_stats['healing']['lifesteal'] * self.multipliers['healing']['lifesteal_multiplier']),
            }
        }
        
        self.history = {
            'round': { 'last': 0, 'total_rounds_played': 0, 'total_rounds_blocked': 0 },
            'hp':    { 'lost': 0, 'healed': 0, 'drained': 0},
            'mp':    { 'lost': 0, 'regenerated': 0, 'drained': 0},
            'damage':     { 'highest': 0, 'last_done': 0, 'total': 0, 'last_target': 0 },
            'healing':    { 'highest': 0, 'last_done': 0, 'total': 0, 'last_target': 0 },
            'resistance': { 'highest': 0, 'last_received': 0, 'total': 0, 'last_agressor': 0},
            'state':      { 'last_debuff': 0, 'last_buff': 0, 'tormentor': 0, 'guardian': 0 },
            'actions': {
                'passive': { 
                    'main': { 'name': None, 'times_activated': 0 },
                    'family': { 'name': None, 'times_activated': 0 },
                },
                'active': {
                    'sk_0':   { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                    'sk_1':   { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                    'sk_2':   { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                    'sk_3':   { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                    'sk_ult': { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                }
            },
        }
    
    def action_reset(self):
        self.action_stats = {
            'hp': { 
                'original': (self.main_stats['hp']['original'] * self.multipliers['hp']['original_hp_multiplier']) + self.multipliers['hp']['original_hp_bonus'],
                'maximum': (self.main_stats['hp']['maximum'] * self.multipliers['hp']['maximum_hp_multiplier']) + self.multipliers['hp']['maximum_hp_bonus'],
                  },
            'mp': {
                'original': (self.main_stats['mp']['original'] * self.multipliers['mp']['maximum_mp_multiplier']) + self.multipliers['mp']['maximum_mp_bonus'],
                'maximum': (self.main_stats['mp']['maximum'] * self.multipliers['mp']['maximum_mp_multiplier']) + self.multipliers['mp']['maximum_mp_bonus'],
                'recover': (self.main_stats['mp']['recover'] * self.multipliers['mp']['recovery_mp_multiplier']) + self.multipliers['mp']['recovery_mp_bonus'],
            },
            'damage': {
                'cr_rate': (self.main_stats['damage']['cr_rate'] * self.multipliers['damage']['cr_rate_multiplier']) + (self.multipliers['damage']['cr_rate_bonus'] / 100),
                'cr_damage': (self.main_stats['damage']['cr_damage'] * self.multipliers['damage']['cr_damage_multiplier']),
            },
            'resistance': {
                'resistance': (self.main_stats['resistance']['resistance'] * self.multipliers['resistance']['resistance_multiplier']),
            },
            'healing': {
                'healing': (self.main_stats['healing']['healing_base'] * self.multipliers['healing']['healing_multiplier']),
                'lifesteal': (self.main_stats['healing']['lifesteal'] * self.multipliers['healing']['lifesteal_multiplier']),
            }
        }