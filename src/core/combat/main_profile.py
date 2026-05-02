
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
                },
            'mp': { 
                'original': self.attr.main['mp'], 
                'maximum': self.attr.main['mp'], 
                'current': self.attr.main['mp'], 
                'recover': 0,
                },
            'damage': {
                'cr_rate': ((5 + (self.attr.main['lky'] / 10)) / 100), 
                'cr_damage': ((150 + (self.attr.main['dex'] / 10)) / 100),
            },
            'resistance': {
                'resistance': self.attr.main['res'] / 2,
            },
            'healing': {
                'healing_base': self.attr.main['knw'],
                'lifesteal': 0,
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
    