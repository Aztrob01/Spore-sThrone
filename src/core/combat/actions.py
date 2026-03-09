import pygame, random
from core.inputs import InputManager

class ActionSystem:
    def __init__(self, user, buffer, eventtoken):
        self.user   = user
        self.buffer = buffer
        self.event  = eventtoken
        self.info   = {
            'action': {
                'selected': False,
                'number': 0,},
            'target': {
                'selected': False,
                'number': 0,}
        }

    def actions(self):
        buttons = InputManager(self.event)
        anumber = self.info['action']['number']

        if buttons.horizontalup() is True:
            if self.info['action']['number'] <= 0:
                self.info['action']['number'] = len(self.user.history.skills) - 1
            else:
                self.info['action']['number'] -= 1
        elif buttons.horizontalup() is False:
            if self.info['action']['number'] >= len(self.user.history.skills) - 1:
                self.info['action']['number'] = 0
            else:
                self.info['action']['number'] += 1

        if anumber != self.info['action']['number']:
            print(f"Selected action: {self.user.history.skills[self.info['action']['number']]}")

        if buttons.confirmup():
            self.info['action']['selected'] = True
    
    def targeting(self):
        buttons = InputManager(self.event)
        tnumber = self.info['target']['number']

        if buttons.verticalup() is True:
            if self.info['target']['number'] <= 0:
                self.info['target']['number'] = len(self.buffer.info_enemies['enemies']) - 1
            else:
                self.info['target']['number'] -= 1
        elif buttons.verticalup() is False:
            if self.info['target']['number'] >= len(self.buffer.info_enemies['enemies']) - 1:
                self.info['target']['number'] = 0
            else:
                self.info['target']['number'] += 1

        if tnumber != self.info['target']['number']:
            print(f"Selected target: {self.buffer.info_enemies['enemies'][self.info['target']['number']]}")

        if buttons.confirmup():
            self.info['target']['selected'] = True
            return True

    def play(self):
        if not self.info['action']['selected']:
            self.actions()
        else:
            if self.targeting():
                self.info['action']['selected'] = False
                self.info['target']['selected'] = False
                return True