import pygame, random

from core.combat_engine import CombatEngine
from core.manager_save  import SaveManager
from core.manager_level import LevelBuilder

class PlayerBuilder:
    def __init__(self, data_player):
        print(data_player)
        self.data_player = data_player

    def generate_team(self):
        from root.registry import CLASSES

        pass
        

class FlowManager:
    def __init__(self, player, level):
        self.__display = pygame.display.get_surface()
        self.__player  = PlayerBuilder(player)
        self.__level   = LevelBuilder(level)
        
        self.__explore = None 
        self.__combat  = CombatEngine()
        self.__state   = [0, 'fight']
        
        self.events  = None

    def load(self):
        pass

    def play(self):
        pass
