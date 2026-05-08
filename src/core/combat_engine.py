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
            'positions': {
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

    def __idle_positionate(self, targets, side):
        positions = {
                'l': { 0: (0.195, 0.550), 1: (0.149, 0.64), 2: (0.1, 0.725), 3: (0.255, 0.6),
                4: (0.22, 0.68), 5: (0.170, 0.627)},
                'r': { 0: (0.800, 0.550), 1: (0.85, 0.64), 2: (0.9, 0.725), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
            }
        
        if side == 'l' and len(targets) < 3:
            import random
            default = [0, 1, 2, 3, 4]
            for num, target in enumerate(targets):
                rand = random.choice(default)
                target.sprite.idle_position = positions[side][rand]
                default.remove(rand)
        else:
            for num, target in enumerate(targets):
                target.sprite.idle_position = positions[side][num]

    def __mount_profiles(self, targets):
        for unities in targets:
            
            x = []
            for allies in targets:
                if allies is not unities:
                    x.append(allies)
                
            unities.combat_profile = CombatProfileData(unities)
            unities.combat_profile.allies = x


    def __compile(self):
        if self.data['temp']['ready'] is False:

            self.__mount_profiles(self.data['entities'])
            self.__idle_positionate(self.data['entities'], 'l')

            self.data['entities'].sort(key=lambda x: x.sprite.idle_position[0] + x.sprite.idle_position[1])
            

            self.__mount_profiles(self.data['team'])
            self.__idle_positionate(self.data['team'], 'r')
                
            self.__events = CombatEvents()
            self.__events.entities = self.data['entities']
            self.__events.team     = self.data['team']
            
            
            self.data['temp']['ready'] = True


    def roll(self):
        self

    def play(self):
        self.__renderization.draw_background((0, 0))

        for nums, unities in enumerate(self.data['entities']):
            if unities is not None:
                pos = unities.sprite.idle_position
                self.__renderization.draw_entity(unities, (pos[0], pos[1]))
                self.__renderization.draw_lifebar(unities)
        for nums, unities in enumerate(self.data['team']):
            if unities is not None:
                pos = unities.sprite.idle_position
                self.__renderization.draw_entity(unities, (pos[0], pos[1]))
                self.__renderization.draw_lifebar(unities)

        
        
        

    def start(self):
        self.__compile()

        self.play()
        self.__events.play()