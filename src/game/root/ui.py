import pygame
from root.settings import *

#TODO create dicts with any assets path as needed

class UIConstruct:
    def __init__(self):
        self.display    = pygame.display.get_surface()
        self.font_size  = 16
        self.font_color = (255, 255, 255)
        self.font_type  = None
        
        self.state = 'PAUSED'

    def _draw_lifebar(self, user):
        lfb_width = user.size[0]
        lfb_ratio = user.stats['health'] / lfb_width
        pygame.draw.rect(self.display, (50, 0, 0) if user.current_health > 0 else (20, 20, 20), (user.rect[0], user.rect[1], user.rect[2], (HEIGHT * 0.02)))
        pygame.draw.rect(self.display, (0, 255, 50) if user.current_health > (user.stats['health'] * 0.3) else (240, 240, 0), (user.rect[0], user.rect[1], user.current_health / lfb_ratio, (HEIGHT * 0.02)))

        
    def draw_combat(self):
        pass

    def draw_world(self):
        pass


    def draw(self):
        pass