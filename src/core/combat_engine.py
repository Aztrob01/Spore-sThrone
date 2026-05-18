import pygame

from core.view.renderizator import Renderization
from core.manager_events    import CombatEventManager

class CombatEngine:
    def __init__(self):
        self.data = {
            # basic
            'cenary': None,
            'entities': [],
            'team': [],
            # match
            'temp': {'ready': False, 'over': False,
                     'active': [], 'waiting': [], 'loop': 0, 'turn': 0},
            'positions': {
                'l': { 0: (0.195, 0.550), 1: (0.149, 0.64), 2: (0.1, 0.725), 3: (0.255, 0.6),
                4: (0.22, 0.68), 5: (0.170, 0.627)},
                'r': { 0: (0.800, 0.550), 1: (0.85, 0.64), 2: (0.9, 0.725), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
            }
    }
        
        self.__events  = CombatEventManager()
        self.__display = pygame.display.get_surface()
        self.__action_controller       = None
        self.__renderization           = Renderization()

    def __draw(self):
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

    def __load(self):
            self.__idle_positionate(self.data['entities'], 'l')
            self.__idle_positionate(self.data['team'], 'r')

            self.__events.mount_profiles(self.data['entities'])
            self.__events.mount_profiles(self.data['team'])

            self.data['entities'].sort(key=lambda x: x.sprite.idle_position[0] + x.sprite.idle_position[1])

            self.__events.entities = self.data['entities']
            self.__events.team     = self.data['team']
            
            self.data['temp']['ready'] = True

    def __organize_active_list(self):
        key = self.data['temp']['active']
        for entities in self.data['team']:
            if entities in key:
                continue
            if len(key) < 10:
                key.append(entities)
        for entities in self.data['entities']:
            if entities in key:
                continue
            if len(key) < 10:
                key.append(entities)

        key.sort(key=lambda target : target.profile.stats['attributes']['str'])

    def __entity_move(self):
        entity = self.data['temp']['active'][0]
        self.data['temp']['waiting'].append(entity)
        self.data['temp']['active'].remove(entity) 
    
    def play(self):
        if self.data['temp']['ready'] == False:
            self.__load()
        
        if self.data['temp']['loop'] != self.__events.loop:
            self.__events.loop = self.data['temp']['loop']
            self.__events.compile()
            self.__organize_active_list()    

        self.__draw()