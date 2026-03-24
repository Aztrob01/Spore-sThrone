
from core.combat.attributes import Attributes

# Create and control data...


class ProfileData:
    def __init__(self, user):
        self.origin = user
        self.attr   = Attributes(user)

        self.stats = {
            'hp': { 'original': self.attr.main['hp'], 'maximum': self.attr.main['hp'], 'current': self.attr.main['hp'] },
            'damage': {
                'crit_chance': ((5 + (self.attr.main['lky'] / 10)) / 100), 
                'phy_damage_multiplier': 1,
                'mag_damage_multiplier': 1,
                'gen_damage_multiplier': 1,
                'crit_damage': ((150 + (self.attr.main['dex'] / 10)) / 100),
            },
            'resistance': {
                'phy_damage_resistance': self.attr.main['res'] / 2,
                'mag_damage_resistance':  0,
                'gen_damage_resistance':  0,
                'crit_damage_resistance': 0,
                'resistance_multiplier':  1,
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
        
class CombatProfileData:
    def __init__(self, char):
        self.user      = char
        self.user_data = char.job.data
        self.stats     = char.profile.stats
        self.history   = char.profile.history

        for entries in self.history['received']:
            self.history['received'][entries] = 0
        for entries in self.history['dealt']:
            self.history['dealt'][entries] = 0

        self.history['rounds'] = {
            'actual_round': 0, 'rounds_played': 0,
        }
        self.history['interactions'] = {
            'last_target': None, 'last_agressor': 0, 'last_assistance': None, 'last_assisted': None },
    
    def reset(self):
        self.stats = self.user.profile.stats
        self.history = self.user.profile.history
        # reseted entries
        for entries in self.history['received']:
            self.history['received'][entries] = 0
        for entries in self.history['dealt']:
            self.history['dealt'][entries] = 0
        # extra entries
        self.history['rounds'] = {
            'actual_round': 0, 'rounds_played': 0,
        }
        self.history['interactions'] = {
            'last_target': None, 'last_agressor': 0, 'last_assistance': None, 'last_assisted': None },

    def update(self):
        """
            transfer the temporary data to the main profile of character.
        """
        pass


                        
