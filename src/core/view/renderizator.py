import pygame
from core.manager_data import DataLoader

class Renderization:
    def __init__(self):
        self.__display = pygame.display.get_surface()
        self.__loader  = DataLoader()

        self.__world      = None
        self.__background = None
        self.__entity     = None

    def draw_world(self, level, offset):
        pass

    def draw_background(self, pos):
        if self.__background == None:
            background = self.__loader.data_level['battleground']
            background = pygame.image.load(background)
            background = pygame.transform.scale(background, self.__loader.data_settings['video']['actual_res'])
            self.__background = background
        self.__display.blit(self.__background, pos)

    def draw_entity(self, entity, pos):
        entity.sprite.update(entity.state)

        res = self.__loader.data_settings['video']['actual_res']
        if entity.rect is None:
            entity.sprite.rect = entity.sprite.image.get_rect()
        entity.sprite.rect.midbottom = (res[0] * pos[0], res[1] * pos[1])
        self.__display.blit(entity.sprite.image, entity.sprite.rect)

            



