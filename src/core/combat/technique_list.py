from core.combat.technique import Passive, Active, Ultimate, Pact

class Buff:
    def __init__(self, name, value, duration, priority, dealer):
        self.name     = name
        self.priority = priority
        self.dealer   = dealer

        self.value        = value
        self.duration     = duration

    def apply(self, target):
        target.stats[self.target_stats[0], target.stats[1]] += self.value
        if self.duration is not None:
            self.duration -= 1
    




    

        

class ClaireMPSV(Passive):
    def __init__(self, user):
        requirements = {
            0: { 
                'type': 'simple',
                'required': ['user', 'activity'],
                'value': ['fighting', '==', True],
            },
            1: {
                'type': 'simple',
                'required': ['user', 'this_action'],
                'value': ['is_sk', '==', True],
            },
        }
        super().__init__("Nobel Compass", requirements, "Claire's Skills change her posture into Challenger or Retainer. Each skill on this mode has its own effects.")
        self.user = user
        
    def activate(self):
        pass

class AlchPSV(Passive):
    def __init__(self, user):
        name        = 'Alchemist Mastery'
        description = 'The Alchemists know the Mastery and secrets of Mana. Their mana Consuption is decreased while skill damage is increased.'
        super().__init__(name, None, description)
        self.user = user

    def activate(self):
        pass