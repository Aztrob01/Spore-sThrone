import pygame, os
from core.manager_data import DataLoader

# animaSprite generates the image, but does not make the image go throught the game itself

class AnimaSprite:
    def __init__(self, user):
        self.user    = user
        self.path = user.job.data['adress']
        self.state   = user.state
        self.display = pygame.display.get_surface()
        self.loader  = DataLoader()

        self.rect  = None
        self.image = None
        self.dimensions = (self.loader.data_settings['video']['actual_res'][0] * user.job.data['dimensions'], self.loader.data_settings['video']['actual_res'][0] * user.job.data['dimensions'])
    
    def validate(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    def update(self, keywords):
        key = f'{self.path}{keywords[0]}/{keywords[1]}.png'
        skey = f'{self.path}fighting/idle.png'
        if self.validate(key):
            self.image = pygame.image.load(key).convert_alpha()
        else:
            print(f'Error trying to find that model {keywords} for {self.user.job.data['codename']}')
            self.image = pygame.image.load(skey).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.dimensions)

            

