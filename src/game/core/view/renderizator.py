import pygame
from game.root.settings import *

class Renderization:
    def __init__(self):
        self.display = pygame.display.get_surface()

    def image_render(self, contents):
        print('RP-1 called for:', contents)
        self.display.blit(contents[0].image, (contents[1][0], contents[1][1]))

    def object_render(self, contents):
        print('RP-2 called for:', contents)
        self.display.blit(contents[0].image, (contents[1][0], contents[1][1]))

    def complex_render(self, contents, positions):
        print('RP-3 called ISNT READY for:', contents)
        pass


