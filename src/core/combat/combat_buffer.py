class CombatBuffer:
    def __init__(self, user):
        self.user = user
        self.info_round   = { 'actual_round': 0, 'rounds_played': 0}
        self.info_hitted  = { 'get_hitted': 0, 'total_damage_mitigated': 0, 'min_received': 0, 'max_received': 0, 'actual_source': None, 'last_source': None }
        self.info_allies  = { 'allies': [] }
        self.info_enemies = { 'enemies': [] }

        self.info_damage  = { 'total_damage_dealt': 0, 'last_target': None, 'min_damage': 0, 'max_damage': 0 }
        self.info_heal    = { 'total_healed_self': 0, 'last_ally_healed': None, 'total_healed_allies': 0, 'total_healed': 0, 'min_heal': 0, 'max_heal': 0 }

        # ----------------

        self.info_basic_attack = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'min_damage': 0, 'max_damage': 0, 'last_target': None }
        self.info_passive      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_1      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_2      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_3      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_4      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }

    def targetreset(self): # this, here, is util? Nah
        if self.info_round['actual_round'] >= (self.info_hitted['get_hitted'] + 1):
            self.info_hitted['actual_source'] = None

    def reset(self):
        self.info_round   = { 'actual_round': 0, 'total_rounds': 0, 'rounds_played': 0}
        self.info_hitted  = { 'get_hitted': 0, 'get_hitted_by': None }
        self.info_allies  = { 'allies': [] }
        self.info_enemies = { 'enemies': [] }

        self.info_damage     = { 'total_damage_dealt': 0, 'last_target': None, 'min_damage': 0, 'max_damage': 0 }
        self.info_heal       = { 'total_healed_self': 0, 'last_ally_healed': None, 'total_healed_allies': 0, 'total_healed': 0, 'min_heal': 0, 'max_heal': 0 }
        self.info_resistance = { 'total_damage_mitigated': 0, 'last_source': None }

        # ----------------

        self.info_basic_attack = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'min_damage': 0, 'max_damage': 0, 'last_target': None }
        self.info_passive      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_1      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_2      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_3      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }
        self.info_skill_4      = { 'times_used': 0, 'total_damage': 0, 'total_heal': 0, 'total_blocked': 0, 'min_damage': 0, 'max_damage': 0, 'min_healed': 0, 'max_healed': 0, 'last_target': None }

    def update(self, target): # transfer buffer data to target.history
        for name, value in self.__dict__.items(): # chech items/variables in buffer
            if isinstance(value, dict): # * if the value format is a dict... 
                if name in target.history: # * ... if the name in dict are in target.history too
                    for key, val in value.items(): # * search for keys/new values in the values 
                        if key in target.history[name]: # if the key are in target.history[name] too
                            target.history[name][key] += val # apply the new value to target.history
    
        