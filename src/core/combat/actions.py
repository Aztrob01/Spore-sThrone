import pygame, random
from src.core.manager_inputs import inputManager

class Passive:
    def __init__(self, name):
        self.name = name

class Pact:
    def __init__(self, name, description, conditions):
        self.name        = name
        self.description = description
        self.conditions  = conditions

        self.type        = "Pact"
        

    def upload(self):
        return # ainda não tá pronto

class Active:
    def __init__(self, name, type):
        pass

class vote_01(Pact):
    def __init__(self, user):
        self.user = user
        codename  = self.user.job.data['info']['codename']
        name        = 'Agony Rhythm'
        description = f'{codename} sacrifices their own health to receive damage multiplication.'
        cl_01_cp = self.user.profile.stats['hp']['original'] # cópia para restauração do HP original
        cl_01    = True if self.user.profile.stats['hp']['maximum'] > cl_01_cp else False
        conditions  = { 'self': { 0: None}, 'fight': None, 'use': None }
        super().__init__(name, description, conditions)
        





skills = {
    'passive':{},
    'pacts': {},
    'skills': {},
    'ultimate': {}     
}