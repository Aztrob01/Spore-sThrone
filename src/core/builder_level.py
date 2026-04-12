from core.unities.entities.entities import Entities
from root.registry import ENEMIES
import random

class LevelBuilder:
    def __init__(self, data_level):
        self.data_level = data_level

    def generate_battleground(self):
        background = self.data_level['battleground']
        return background
    
    def generate_enemies(self):
        print(self.data_level)
        slots  = random.randint(2, 5)
        entry = []

        for ents in self.data_level['enemies']:
            entry.append(self.data_level['enemies'][ents])

        for numbers, monsters in enumerate(entry):
            for nums, ents in enumerate(ENEMIES):
                if entry[numbers][0] not in ENEMIES:
                    print('Removing', entry[numbers][0], 'from list')
                    entry.remove(entry[numbers])

        entry.sort(key=lambda target: target[2])

        output = []

        for i in range(1, slots):
            i = i - 1
            print('--------------------------------')
            ch = random.uniform(0, 1)
            ch = round(ch, 2)
            print(f'Dinamic entrance started with {i}, {ch}% in a total of {slots} tries' )

            for objects in entry:
                print('-----------------------------\nChecking for objects in entry. Value', objects)
                if ch <= objects[2]:
                    
                    obj = Entities(ENEMIES[objects[0]]())
                    print(f'{ch}% defined for {obj.job.data['info']['codename']}')
                    obj.profile.stats['level']['current'] = random.randint(objects[1][0], objects[1][1])
                    print('Entity Object created.')
                    output.append(obj)
                    print(output)
                    print(f'Appended {obj.job.data['info']['codename']} at position {i} with level {obj.profile.stats['level']['current']}')
                    print(f'{obj.job.data['info']['codename']} absorved {ch}% to appear from {objects[2]}%')
                    break
        
        
        if len(output) == 0:
            for objects in entry:
                print("Value break. Creating an random creature for guarantee.")
                obj = Entities(ENEMIES[objects][0]())
                obj.profile.stats['level']['current']= random.randint(objects[1][0], objects[1][1])
                output.append(obj)
                print('Emergency Entity Created.')
                break
                
        
        return output
