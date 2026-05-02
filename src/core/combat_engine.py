import pygame

from core.view.renderizator import Renderization
from core.manager_events    import CombatEvents
from core.combat.combat_profile import CombatProfileData


class CombatEngine:
    def __init__(self):
        self.data = {
            # basic
            'cenary': None,
            'entities': [],
            'team': [],
            # match
            'temp': {'ready': False, 'over': False,
                     'turns': [], 'active': 0, 'turn': 0 },
            'positions': { # 460 -> 510 
                'l': { 0: (0.195, 0.550), 1: (0.149, 0.64), 2: (0.1, 0.725), 3: (0.255, 0.6),
                4: (0.22, 0.68), 5: (0.170, 0.627)},
                'r': { 0: (0.800, 0.550), 1: (0.85, 0.64), 2: (0.9, 0.725), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
            }
    }
        

        self.__events  = None
        self.__display = pygame.display.get_surface()
        self.__action_controller       = None
        self.__renderization           = Renderization()

    def __compile(self):
        if self.data['temp']['ready'] is False:
            for unities in self.data['entities']:
                x = []
                for allies in self.data['entities']:
                    if allies != unities:
                        x.append(allies)
                
                unities.combat_profile = CombatProfileData(unities)
                unities.combat_profile.allies = x
                print(unities.combat_profile.action_stats['damage']['cr_rate'], unities.job.data['name'])
            
            for unities in self.data['team']:
                
                x = []
                for allies in self.data['team']:
                    if allies != unities:
                        x.append(allies)
                
                unities.combat_profile = CombatProfileData(unities)
                unities.combat_profile.allies = x
                print(unities.combat_profile.action_stats['damage']['cr_rate'], unities.job.data['name'])

            self.__events = CombatEvents()
            self.__events.entities = self.data['entities']
            self.__events.team     = self.data['team']
    
            return True
        return False

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
        
        

    def start(self):
        if self.__compile():
            self.data['temp']['ready'] = True
        self.play()