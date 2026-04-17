import pygame

class inputManager:
    def __init__(self, eventlist):
        self.events = eventlist
        
    def key_up(self, key):
        for events in self.events:
            if events.type == pygame.KEYUP and events.key == key:
                return True
    
    def key_dw(self, key):
        for events in self.events:
            if events.type == pygame.KEYDOWN and events.key == key:
                return True
            
    def key_mult_up(self, k_negative, k_positive):
        for events in self.events:
            if events.type == pygame.KEYUP and events.key == k_negative:
                return False
            if events.type == pygame.KEYUP and events.key == k_positive:
                return True
        return False
    
    def key_mult_dw(self, k_negative, k_positive):
        for events in self.events:
            if events.type == pygame.KEYDOWN and events.key == k_negative:
                return False
            if events.type == pygame.KEYDOWN and events.key == k_positive:
                return True
        return False
    
