import pygame

from core.view.renderizator import Renderization
from core.manager_events    import CombatEvents
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
            'positions': { # 460 -> 510 
                'l': { 0: (0.195, 0.550), 1: (0.149, 0.64), 2: (0.1, 0.725), 3: (0.255, 0.6),
                4: (0.22, 0.68), 5: (0.170, 0.627)},
                'r': { 0: (0.800, 0.550), 1: (0.85, 0.64), 2: (0.9, 0.725), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
            }
        }
        

        self.__events  = CombatEvents()
        self.__display = pygame.display.get_surface()
        self.__action_controller       = None
        self.__renderization           = Renderization()

    def __prepare(self):
        if self.data['temp']['active'] is False:
            for nums, unities in enumerate(self.data['entities']):
                self.data['temp']['entities'][nums] = CombatProfileData(unities)
            for nums, unities in enumerate(self.data['team']):
                self.data['temp']['chars'][nums] = CombatProfileData(unities)
            
            self.data['temp']['active'] = True

    def roll(self):
        self

    def play(self):
        self.__renderization.draw_background((0, 0))

        for nums, unities in enumerate(self.data['entities']):
            if unities is not None:
                pos = self.data['positions']['l'][nums]
                self.__renderization.draw_entity(unities, (pos[0], pos[1]))
                self.__renderization.draw_lifebar(unities)
        for nums, unities in enumerate(self.data['team']):
            if unities is not None:
                pos = self.data['positions']['r'][nums]
                self.__renderization.draw_entity(unities, (pos[0], pos[1]))
                self.__renderization.draw_lifebar(unities)