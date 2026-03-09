import pygame

from core.root.settings import *
from core.level_engine    import LevelEngine

# * Main Game Loop

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.m_name = pygame.display.set_caption('Dragon Rose')
        self.events = pygame.event.get() # * starts geting an obsolete value just to initialize self.level correctly
        self.clock  = pygame.time.Clock()  
        self.level  = LevelEngine(self.events)

    def run(self):
        while True:
            self.events = pygame.event.get() # * update events until call anything 
            # ? print(events)
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

            self.level.play()

            pygame.display.update()
            self.clock.tick(GAMECLOCK)

game = Game()
if __name__ == '__main__':
    game.run()