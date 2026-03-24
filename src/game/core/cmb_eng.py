import pygame

from game.core.view.renderizator import Renderization


class CombatEngine:
    def __init__(self, level_data, player_data, event_data):
        # info
        self.level  = level_data
        self.player = player_data
        self.events = event_data
        self.info   = {
            'cache': {},
            'match': { 'rounds_played': 0, 'is_game_over': False }
        }
        # mech
        self.display = pygame.display.get_surface()
        self.actions = None # need to be changed later for ActionSystem
        self.render  = Renderization()

    def mount(self): # 1st: mount the combat entities, teams, etc
        pass

    def active(self): # 2nd: create and active entities Combat Cached Profiles
        pass