class CombatProfileData:
    def __init__(self, char):
        self.user      = char
        self.user_data = char.job.data
        self.stats     = char.profile.stats
        self.allies  = {}
        self.enemies = {}
        
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
        pass