from core.combat.technique import Passive, Active, Ultimate, Pact

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
        if self.user.combat_profile.stats['state']
