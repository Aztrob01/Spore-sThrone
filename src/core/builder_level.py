from core.unities.entities.entities import Entities
from root.registry import ENEMIES
import random

class LevelBuilder:
    def __init__(self, data_level):
        self.data_level = data_level

    def generate_battleground(self):
        background = self.data_level['battleground']
        return background
    
    def generate_enemies(self, value=0):
        if value > 5:
            raise ValueError('The value input is higher than 5.')
        
        slots = value if value > 0 else random.randint(2, 5)
        output = []

        entities = []
        for nums in self.data_level['enemies']:
            entities.append(self.data_level['enemies'][nums])

        entities.sort(key=lambda target : target[2])

        enemies = []
        for nums in ENEMIES:
            enemies.append(ENEMIES[nums])

        for slot in range(slots):
            chance = round(random.uniform(0.01, 1), 2)
            
            for ents in entities:
                if chance > entities[-1][2]:
                    cache = Entities(random.choice(enemies)())
                    cache.profile.stats['level']['current'] = random.randint(5, 10)
                    output.append(cache)
                    break
                
                if ents[0] not in ENEMIES:
                    continue

                if chance <= ents[2]:
                    cache = Entities(ENEMIES[ents[0]]())
                    level = random.randint(ents[1][0], ents[1][1])
                    cache.profile.stats['level']['current'] = level
                    output.append(cache)
                    break
                
        return output

        
            