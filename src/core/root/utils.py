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

def update_sprt(target): #! will break with the changes on image_load() / 15:37
    for states in target.origin.inner_galery:
        if target.main_state != 'fighting':
            target.sprite = target.origin.inner_galery[target.main_state]
        else:
            target.sprite = target.origin.inner_galery[target.main_state][target.fighting_state]

    target.sprite = pygame.transform.scale(target.sprite, (target.on_screen))
    target.rect = target.sprite.get_rect()
    target.size = target.sprite.get_size()

# ------------------------------------------------------------
# Image Loader, to load and scale images based on the given path

def image_load(origin, size):
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
