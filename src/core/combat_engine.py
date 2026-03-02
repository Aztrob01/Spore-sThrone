import pygame
from root.settings import *
from combat.actions import ActionSystem
from core.team_engine import TeamEngine

class CombatEngine:
    def __init__(self, level, player):
        self.level    = level
        self.player   = player
        
        self.display    = pygame.display.get_surface()
        self.actions    = ActionSystem
        self.animator   = None
        self.background = self.level.static['background']

        creatures    = self.level.creatures_randomize(5) #* 5 is the number of unities that must be returned by randomize
        self.team_0  = TeamEngine(creatures)
        self.team_1  = TeamEngine(player.chars)
        self.defined = False    
        # ------------------------------
        self.positions = {
            'left': {
                0: (0.195, 0.460), 1: (0.106, 0.643), 2: (0.154, 0.551), 3: (0.28, 0.51),
                4: (0.106, 0.643), 5: (0.170, 0.627) },
            'right': {
                0: (0.800, 0.460), 1: (0.847, 0.551), 2: (0.895, 0.643), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
        }
        # -------------------------------
        self.info = {
            'rounds_played': 0,
            'actual_side': 'right', #players turn first
            'game_over': False,
            'win_side': None
        }

    def define(self):
        if not self.defined:
            self.team_0.define()
            self.team_1.define()
            self.defined = True # first, define the main unities in a team
        
    def draw(self):
        self.display.fill((0, 0, 0)) # self.display.blit((self.background), (0, 0))
        for nums, unities in enumerate(self.team_0.active_unities):
            unities.rect.midbottom = ((WIDTH * self.positions['left'][nums][0]), (HEIGHT * self.positions['left'][nums][1]))
        for nums, unities in enumerate(self.team_1.active_unities):
            unities.rect.midbottom = ((WIDTH * self.positions['right'][nums][0]), (HEIGHT * self.positions['right'][nums][1]))
        
    def fight(self):
        if self.info['actual_side'] == 'left':
            if self.actions(self.team_1.active_unity).play():
                if self.team_1.next() is False:
                    self.info['actual_side'] = 'right'
        else: # after the player turn, the enemy turn starts
            if self.actions(self.team_0.active_unity).play():
                if self.team_0.next() is False: # if the next function returns false, it means that the turn of the team is over
                    self.info['actual_side'] = 'left'
                    self.info['rounds_played'] += 1


    def start(self):
        self.define()
        self.draw()
        if not self.info['game_over']:
            self.fight()