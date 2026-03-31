import pygame, json, os, datetime

#? This code was built using Pygame Lib and Better Comments Extension (VS Code)
from core.manager_flow  import FlowManager
from core.manager_data import DataLoader

class GameLoop:
    def __init__(self):
        self.__loader = DataLoader()
        self.__screen = pygame.display.set_mode((self.__loader.data_settings['video']['actual_res'][0], self.__loader.data_settings['video']['actual_res'][1]))
        self.__m_name = pygame.display.set_caption("Spore's Throne")
        self.__debug  = None
        self.__clock  = pygame.time.Clock()

        self.level    = FlowManager(self.__loader.data_player, self.__loader.data_level)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)    


            self.level.events = events

            self.level.play()
            pygame.display.update()

            self.__clock.tick(self.__loader.game['clock'])

# ------------------------

game = GameLoop()
game.run()


