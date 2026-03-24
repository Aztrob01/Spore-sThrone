import pygame
from root.settings import *

pygame.init()

class Debugger:
    def __init__(self, font_size=16):
        self.display = pygame.display.get_surface()
        self.font    = pygame.font.Font(None, font_size)
        self.start_pos = (10, 10)
        self.color   = [255, 255, 255]
        self.padding = 5
        self.line_height = font_size * 0.7

    def _draw_hitbox(self, target):
            if target.main_state != 'defeated':
                pygame.draw.rect(self.display, (255, 255, 255), target.rect, 1)

    def combat_draw(self, target):
        def _draw_data():
            x = target.rect[0] + target.rect[2] + 5
            y = (target.rect[1])
            data = {
                'name': target.origin_type,
                'States': (target.main_state, target.secondary_state),
                'health': f" {target.current_health} / {target.stats['health']}",
                'Passive / Times Used': (target.passive, target.passive_times), 
            }

            for key, value in data.items():
                text = f'{key}: {value}'
                display = self.font.render(text, True, self.color, (0, 0, 0))
                self.display.blit(display, (x, y))
                y += self.line_height
            
        
        _draw_data()
        # self._draw_hitbox(target)
