

class CombatEvents:
    def __init__(self):
        self.entities = []
        self.team     = []

        self.before_events = []
        self.while_events  = []
        self.after_events  = []

        self.round = 0
        self.last_round_compiled = None

    def sort_by_priority(self, target_event):
        target_event.sort(key=lambda target : target[0].priority)

    def compile(self):
        if self.last_round_compiled != self.round:
            for unities in self.entities:

                if len(unities.combat_profile.status['passives']) > 0:
                    for passives in unities.combat_profile.status['passives']:
                        if passives != None:
                            match passives.priority:
                                case 1 | 2 | 3:
                                    self.before_events.append([passives, unities])
                                case 4 | 5 | 6:
                                    self.while_events.append([passives, unities])
                                case 7 | 8 | 9:
                                    self.after_events.append([passives, unities])

                if len(unities.combat_profile.status['buffs']) > 0:
                    for buffs in unities.combat_profile.status['buffs']:
                        if buffs is not None:
                            match buffs.priority:
                                case 1, 2, 3:
                                    self.before_events.append([buffs, unities])
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
            

            for objects in self.before_events:
                print(f'Eventos de começo: {objects[0].name} de prioridade {objects[0].priority} do {objects[1].codename}')
            for objects in self.while_events:
                print(f'Eventos de combate: {objects[0].name} de prioridade {objects[0].priority} do {objects[1].codename}')
            for objects in self.after_events:
                print(f'Eventos de finalização: {objects[0].name} de prioridade {objects[0].priority} do {objects[1].codename}')
            self.update_events(self.before_events)
            self.last_round_compiled = self.round

    def update_events(self, target_events):
        from core.combat.common_buffs import BuffModel
        from core.combat.common_passives import PassiveModel

        for events in target_events:
            if issubclass(events[0], BuffModel):
                events.update()
            elif issubclass(events[0], PassiveModel):
                if events.update() == False:
                    print(f'Passiva {events[0].name} de {events[1].job.name} não pode ser ativada de maneira imediata')
            else:
                events[0].update()


    def play(self):
        self.compile()
        
        