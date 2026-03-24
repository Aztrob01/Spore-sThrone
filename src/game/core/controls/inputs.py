import pygame

class InputManager:
    def __init__(self, event):
        self.event = event

    def horizontalup(self):
        for event in self.event:
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                return True
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                return False
            else:
                return None
        
    def verticalup(self):
        for event in self.event:
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                return True
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                return False
            else:
                return None
    
    def confirmup(self):
        for event in self.event:
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                return True