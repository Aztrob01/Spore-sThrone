

class CombatEventManager:
    def __init__(self):
        self.entities = []
        self.team     = []

        self.before_events = []
        self.while_events  = []
        self.after_events  = []

        self.loop = None

    def mount_profiles(self, targets):
        from core.combat.combat_profile import CombatProfileData
        
        for unities in targets:
            
            x = []
            for allies in targets:
                if allies is not unities:
                    x.append(allies)
                
            unities.combat_profile = CombatProfileData(unities)
            unities.combat_profile.allies = x
                
    def priority_sort(self, target_event):
        target_event.sort(key=lambda target : target[0].priority)

    def update_events(self, target_events):
        from core.combat.common_buffs import BuffModel
        from core.combat.common_passives import PassiveModel

        for objects in target_events:
            if objects.update() == False:
                print(f'Removing {objects.name} from queue')
                target_events.remove(objects)

    def check_conditions(self, target):
        x = False

        for events in self.while_events:
            if events.conditions(target):
                x = True
                events.update()
        return x 

    def compile(self):
        creatures = []
        for unities in self.entities:
            creatures.append(unities)
        for unities in self.team:
            creatures.append(unities)

        for unities in creatures:
            path = unities.combat_profile.status
            
            for key in path:
                for items in path[key]:
                    if items != None:
                        object = items(unities)
                        match object.buff_data['priority_level']:
                            case 1 | 2 | 3:
                                if object not in self.before_events:
                                    self.before_events.append(object)
                            case 4 | 5 | 6:
                                if object not in self.while_events:
                                     self.while_events.append(object)
                            case 7 | 8 | 9:
                                if object not in self.after_events:
                                     self.after_events.append(object)

        self.update_events(self.before_events)
