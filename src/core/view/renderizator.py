import pygame
from core.manager_data import DataLoader

class Renderization:
    def __init__(self):
        self.__display = pygame.display.get_surface()
        self.__loader  = DataLoader()

        self.__world      = None
        self.__background = None
        self.__entity     = None

        self.__ui  = None
        self.__gfx = None
        
    def draw_world(self, level, offset):
        pass

    def draw_background(self, pos):
        if self.__background == None:
            background = self.__loader.data_level['battleground']
            background = pygame.image.load(background)
            background = pygame.transform.scale(background, self.__loader.data_settings['video']['actual_res'])
            self.__background = background
        self.__display.blit(self.__background, pos)

    def draw_shadow(self, center_pos):
        path = './src/assets/image/general/Shadow1.png'
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale_by(img, 4)
        rect = img.get_rect()
        rect.center = center_pos
        self.__display.blit(img, rect)
    
    def draw_lifebar(self, owner):
        red   = (30, 0, 0)
        green = (20, 210, 30)
        grey  = (60, 60, 60)

        rect = owner.sprite.rect
        size = (rect[2], rect[3])
        original = owner.profile.stats['hp']['original']
        maximum = owner.profile.stats['hp']['maximum']
        current = owner.profile.stats['hp']['current'] / maximum 

        grey  = pygame.draw.rect(self.__display, grey, (rect.bottomleft[0], rect.midtop[1], size[0], size[1] / 10))
        red   = pygame.draw.rect(self.__display, red, (rect.bottomleft[0], rect.midtop[1], size[0] * (maximum / original), size[1] / 10))
        green = pygame.draw.rect(self.__display, green, (rect.bottomleft[0], rect.midtop[1], (size[0] * current), size[1] / 10))

    def draw_entity(self, entity, pos):
        entity.sprite.update(entity.state)

        res = self.__loader.data_settings['video']['actual_res']
        pos = (res[0] * pos[0], res[1] * pos[1])

        if entity.rect is None:
            entity.sprite.rect = entity.sprite.image.get_rect()
            
        entity.sprite.rect.midbottom = pos
        self.draw_shadow(pos)
        self.__display.blit(entity.sprite.image, entity.sprite.rect)

            



