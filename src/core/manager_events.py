

class CombatEvents:
    def __init__(self):
        self.entities = []
        self.team     = []

        self.before_events = []
        self.while_events  = []
        self.after_events  = []

        self.round = 0
        self.last_round_compiled = None

    def priority_phase(self, target_event=[]):
        target_event.sort(key=lambda target : target.priority)
            

    def compile(self):
        if self.last_round_compiled != self.round:
            for unities in self.entities:

                if len(unities.combat_profile.status['passives']) > 0:
                    for passives in unities.commbat_profile.status['passives']:
                        if passives is not None:
                            match passives.priority:
                                case 1, 2, 3:
                                    self.before_events.append([passives, unities])
                                case 4, 5, 6:
                                    self.while_events.append([passives, unities])
                                case 7, 8, 9:
                                    self.after_events.append([passives, unities])

                if len(unities.combat_profile.status['buffs']) > 0:
                    for buffs in unities.combat_profile.status['buffs']:
                        if buffs is not None:
                            match buffs.priority:
                                case 1, 2, 3:
                                    buffs.apply(unities)
                                case 4, 5, 6:
                                    self.while_events.append([buffs, unities])
                                case 7, 8, 9:
                                    self.after_events.append([buffs, unities])
                                case _:
                                    raise ValueError(f'Buff {buffs.name} has a invalid priority value')
                    
                if len(unities.combat_profile.status['debuffs']) > 0:
                    for debuffs in unities.combat_profile.stats['debuffs']:
                        if debuffs is not None:
                            match debuffs.priority:
                                case 1, 2, 3:
                                    debuffs.apply(unities)
                                case 4, 5, 6:
                                    self.while_events.append([debuffs, unities])
                                case 7, 8, 9:
                                    self.after_events.append([debuffs, unities])
                    
            self.last_round_compiled = self.round

    def       



        
