
from core.combat.attributes import Attributes

# Create and control data...


class ProfileData:
    def __init__(self, user):
        self.origin = user
        self.attr   = Attributes(user)
        
        self.state = ['fighting', 'idle']
        self.stats = {
            'hp': { 
                'original': self.attr.main['hp'], 
                'maximum': self.attr.main['hp'], 
                'current': self.attr.main['hp'], 
                'extra': 0,
                
                'original_hp_multiplier': 1,
                'maximum_hp_multiplier': 1,
                'extra_hp_multiplier': 1,

                'original_hp_bonus': 0,
                'maximum_hp_bonus': 0,
                'extra_hp_bonus': 0,
                },
            'mp': { 
                'original': self.attr.main['mp'], 
                'maximum': self.attr.main['mp'], 
                'current': self.attr.main['mp'], 
                'recover': 0,

                'original_mp_multiplier': 1,
                'maximum_mp_multiplier': 1,
                'extra_mp_multiplier': 1,
                'recover_multiplier': 1,

                'original_mp_bonus': 0,
                'maximum_mp_bonus': 0,
                'recover_bonus': 0,
                },
            'damage': {
                'cr_damage_chance': ((5 + (self.attr.main['lky'] / 10)) / 100), 
                'cr_damage_value': ((150 + (self.attr.main['dex'] / 10)) / 100),
                
                'sk_damage_multiplier': 1,
                'ab_damage_multiplier': 1,
                'cr_damage_multiplier': 1,

                'sk_damage_bonus': 0,
                'ab_damage_bonus': 0,
                'cr_damage_bonus': 0,
            },
            'resistance': {
                'resistance': self.attr.main['res'] / 2,
                'ab_resistance_multiplier': 1,
                'sk_resistance_multiplier': 1,
                'cr_resistance_multiplier': 1,

                'ab_resistance_bonus': 0,
                'sk_resistance_bonus': 0,
                'cr_resistance_bonus': 0,
            },
            'healing': {
                'healing_base': self.attr.main['knw'],
                
                'healing_multiplier': 1,
                'healing_receive_multiplier': 1,

                'healing_bonus': 0,
                'healing_receive_bonus': 0,
            },
            'status': {
                'buffs': [],
                'debuffs': [],
            },
            'level': { 'current': 1, 'exp': 0, 'total_exp': 0, 'max_level': 99 }
            }
        
        self.history = { 
            'received': {
                'total_damage_mitigated': 0, 'mitigated_by_skills': 0, 'highest_damage_received': 0,
                'total_healing_received': 0, 'highest_healing_received': 0
            },
            'dealt': {
                'total_damage_dealt': 0, 'damage_by_skills': 0, 'highest_damage_dealt': 0,
                'total_healing_dealt': 0, 'healing_by_skills': 0, 'highest_healing_dealt': 0,
            },
            'actions': {
                'ba_times_used': 0,
                '1st_sk_times_used': 0, 
                '2nd_sk_times_used': 0,
                '3rd_sk_times_used': 0,
                '4rd_sk_times_used': 0,
            }
        }
    