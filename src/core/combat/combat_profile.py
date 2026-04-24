class CombatProfileData:
    def __init__(self, char):
        self.user      = char
        self.user_data = char.job.data
        self.stats     = char.profile.stats
        self.allies  = {}
        self.targets = {}
        
        self.history = {
            'last_round_played': 0,
            'hp': { 'lost': 0, 'healed': 0, 'drained': 0},
            'mp': { 'lost': 0, 'regenerated': 0, 'drained': 0},
            'damage': { 'highest': 0, 'last_done': 0, 'total': 0, 'last_target': 0 },
            'healing': { 'highest': 0, 'last_done': 0, 'total': 0, 'last_target': 0 },
            'resistance': { 'highest': 0, 'last_received': 0, 'total': 0, 'last_agressor': 0},
            'state': { 'last_debuff': 0, 'last_buff': 0, 'tormentor': 0, 'guardian': 0 },
            'actions': {
                'passive': { 'times_activated': 0 },
                'sk_0': { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                'sk_1': { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                'sk_2': { 'name': None, 'times_used': 0, 'total_consuption': 0 },
                'sk_3': { 'name': None, 'times_used': 0, 'total_consuption': 0 },
            },
        }
    
    def reset(self):
        pass