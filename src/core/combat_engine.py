import pygame

from core.view.renderizator import Renderization
from core.combat.profile    import CombatProfileData



class CombatEngine:
    def __init__(self):
        self.data = {
            # basic
            'cenary': None,
            'entities': [],
            'team': [],
            # match
            'turn': 0,
            'active': 0,
            'turns': [],
            'over': False,
            # entity cache
            'temp': {
                'active': False,
                'entities': None,
                'chars': None,
            },
            'positions': {
                'l': { 0: (0.195, 0.460), 1: (0.106, 0.643), 2: (0.154, 0.551), 3: (0.28, 0.51),
                4: (0.106, 0.643), 5: (0.170, 0.627)},
                'r': { 0: (0.800, 0.460), 1: (0.847, 0.551), 2: (0.895, 0.643), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
            }
        }
        

        self.events  = None
        self.display = pygame.display.get_surface()
        self.action_controller       = None
        self.combatevents_controller = None
        self.renderization = Renderization()

    def __prepare(self):
        if self.data['temp']['active'] is False:
            for nums, unities in enumerate(self.data['entities']):
                self.data['temp']['entities'][nums] = CombatProfileData(unities)
            for nums, unities in enumerate(self.data['team']):
                self.data['temp']['chars'][nums] = CombatProfileData(unities)
            
            self.data['temp']['active'] = True

    def prev(self, target=None):
        pass

    def next(self, target=None):
        pass

    def apply_combat_profile(self):
        pass    

    def update(self):
        pass

    def play(self):
        self.renderization.draw_background((0, 0))

        for nums, unities in enumerate(self.data['entities']):
            if unities is not None:
                pos = self.data['positions']['l'][nums]
                self.renderization.draw_entity(unities, (pos[0], pos[1]))
        for nums, unities in enumerate(self.data['team']):
            if unities is not None:
                pos = self.data['positions']['r'][nums]
                self.renderization.draw_entity(unities, (pos[0], pos[1]))