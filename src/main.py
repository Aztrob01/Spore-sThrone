import pygame

from game.root.settings import *
from game.core.lvl_eng  import LevelEngine

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.m_name = pygame.display.set_caption("Spore's Throne")
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

from game.core.lvl_eng import LevelManager

pm = LevelManager(None)
pm.read('x')

exit(0)

game = Game()
if __name__ == '__main__':
    game.run()

