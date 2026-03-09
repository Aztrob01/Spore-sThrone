import pygame
from root.settings import *
from core.combat.actions import ActionSystem
from core.combat.combat_buffer import CombatBuffer
from core.combat.team_engine import TeamEngine

class CombatEngine:
    def __init__(self, leveldata, player, eventtoken):
        self.loaded = False
        self.level    = leveldata
        self.player   = player
        self.event    = eventtoken
        
        self.display    = pygame.display.get_surface()
        self.actions    = ActionSystem # * like that the values will reset anytime
        self.animator   = None
        self.background = None

        self.team_0  = None
        self.team_1  = None
        # ------------------------------
        self.positions = {
            'left': {
                0: (0.195, 0.460), 1: (0.106, 0.643), 2: (0.154, 0.551), 3: (0.28, 0.51),
                4: (0.106, 0.643), 5: (0.170, 0.627) },
            'right': {
                0: (0.800, 0.460), 1: (0.847, 0.551), 2: (0.895, 0.643), 3: (0.766, 0.611),
                4: (0.721, 0.517) }
        }
        self.buffers = {
            'left': {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            'right': {0: None, 1: None, 2: None, 3: None, 4: None }
        }
        # -------------------------------
        
        self.info = {
            'rounds_played': 0,
            'actual_side': 'right', #players turn first
            'game_over': False,
            'win_side': None
        }

    def define(self):
        if self.loaded is False:
            print(f'Definer is {self.loaded}. Starting combat Engine definer...')
            
            self.background = self.level.battleground

            entities = self.level.entities_randomize(5)
            self.team_0 = TeamEngine(entities)
            self.team_0.define()
            print(f'Entities and team defined as: {entities} -> {self.team_0.active_unities}')
            for nums, unities in enumerate(self.team_0.active_unities):
                unities.rect.midbottom = ((WIDTH * self.positions['left'][nums][0]), (HEIGHT * self.positions['left'][nums][1]))
            self.team_1 = TeamEngine(self.player.chars)
            self.team_1.define()
            print(f'Team player defined as {self.team_1.active_unities}')
            for nums, unities in enumerate(self.team_1.active_unities):
                unities.rect.midbottom = ((WIDTH * self.positions['right'][nums][0]), (HEIGHT * self.positions['right'][nums][1]))
            self.loaded = True
            print(f'Combat succesfully loaded. Load defined as {self.loaded}')
                
    def draw(self):
        self.display.blit((self.background), (0, 0))
        for nums, unities in enumerate(self.team_0.active_unities):
            self.display.blit(unities.image, unities.rect)
        for nums, unities in enumerate(self.team_1.active_unities):
            self.display.blit(unities.image, unities.rect)
        
    def fight(self):
        if self.info['actual_side'] == 'left':
            if self.actions(self.team_1.active_unity, self.buffers['right'][self.team_1.active_unities_index], self.event).play():
                if self.team_1.next() is False:
                    self.info['actual_side'] = 'right'
        else: # after the player turn, the enemy turn starts
            if self.actions(self.team_0.active_unity, self.buffers['left'][self.team_0.active_unities_index], self.event).play():
                if self.team_0.next() is False: # if the next function returns false, it means that the turn of the team is over
                    self.info['actual_side'] = 'left'
                    self.info['rounds_played'] += 1


    def start(self):
        self.define()
        self.draw()
        if not self.info['game_over']:
            self.fight()