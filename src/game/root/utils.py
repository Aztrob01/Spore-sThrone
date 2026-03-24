from root.settings import *
import pygame

# ------------------------------------------------------------
# Background Manager to load and scale Combat Background Image

class BackgroundManager:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))

# ------------------------------------------------------------
# Sprite Updater, to load and scale Entity Sprites based on their state and size

def update_sprite(state, char): #! 
    for mstate in char.job.sprites:
        if mstate == state[0]:
            for sstate in char.job.sprites[mstate]:
                if sstate == state[1]:
                    char.image = pygame.image.load(char.job.sprites[mstate][sstate])
        elif state[0] not in char.job.sprites:
            print(f'Erro na renderização de {mstate} / {sstate} de {char.job.data['info']['cavaliere']}')
            char.image = pygame.image.load(char.job.sprites['fight']['idle'])

    char.image = pygame.image.load(char.image, (char.job.sprites['size']['common']))
    char.rect  = char.image.get_rect()

# ------------------------------------------------------------
# Image Loader, to load and scale images based on the given path

def load_image(origin, size):
    image = pygame.image.load(origin)
    image = pygame.transform.scale(image, size)
    
    return image

# ------------------------------------------------------------
# Timer class to create cooldowns and delays in the combat system
# using pygame's time module

class Timer:
    def __init__(self, delay):
        self.delay = delay
        self.ltime = 0

    def wait(self):
        ctime = pygame.time.get_ticks()
        if ctime - self.ltime > self.delay:
            self.ltime = ctime
            return True
        return False

# ------------------------------------------------------------
