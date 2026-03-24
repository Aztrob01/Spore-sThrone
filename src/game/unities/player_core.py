from entities.characters import Characters
from entities.classes import *

class PlayerCore:
    def __init__(self):
        self.chars = [Characters(cvl()), Characters(dwf()), Characters(wzr())]
        self.wchar = self.chars[0]
        