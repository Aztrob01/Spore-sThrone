
from core.combat.attributes import Attributes

# Create and control data...


class ProfileData:
    def __init__(self, user):
        self.origin = user
        self.attr   = Attributes(user)

        self.stats = {
            'hp': { 'original': self.attr.main['hp'], 'maximum': self.attr.main['hp'], 'current': self.attr.main['hp'] },
            'mp': { 'original': 75, 'maximum': 75, 'current': 75 },
            'damage': {
                'cr_damage_chance': ((5 + (self.attr.main['lky'] / 10)) / 100), 
                'cr_damage_value': ((150 + (self.attr.main['dex'] / 10)) / 100),
                'ph_damage_multiplier': 1,
                'mg_damage_multiplier': 1,
                'ab_damage_multiplier': 1,
            },
            'resistance': {
                'ph_damage_resistance': self.attr.main['res'] / 2,
                'mg_damage_resistance':  0,
                'ab_damage_resistance':  0,
                'cr_damage_resistance': 0,
                'ab_resistance_multiplier':  1,
            },
            'healing': {
                'healing_base': self.attr.main['knw'],
                'healing_multiplier': 1,
                'healing_receive_multiplier': 1,
            },
            'state': {
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
    