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
        slots  = random.randint(1, 5)
        entry = []

        for ents in self.data_level['enemies']:
            entry.append(self.data_level['enemies'][ents])

        for numbers, monsters in enumerate(entry):
            for nums, ents in enumerate(ENEMIES):
                if entry[numbers][0] not in ENEMIES:
                    print('Removing', entry[numbers][0], 'from list')
                    entry.remove(entry[numbers])

        for nums, objs in enumerate(entry):
            if entry[nums][2] < entry[nums - 1][2]:
                x = entry.pop(nums)
                entry.insert((nums - 1) if nums > 0 else 0, x)
                print('Object organized', entry)

        output = []

        for i in range(1, slots + 1):
            i = i - 1
            print(i, slots)
            ch = random.uniform(0, 1)
            ch = round(ch, 2)

            for objects in entry:
                if ch <= objects[2]:
                    obj = Entities(ENEMIES[objects[0]]())
                    obj.profile.stats['level']['current'] = random.randint(objects[1][0], objects[1][1])
                    output.append(obj)
                    print(f'Appended {obj.job.data['info']['codename']} at position {i} with level {obj.profile.stats['level']['current']}')
                    print(f'{obj.job.data['info']['codename']} absorved {ch}% to appear from {objects[2]}%')
        
        # estudei a versão lambda. Ainda não entendi muito bem, mas seria como...
        # entry.sort(lambda target : target[2])
        # vou manter minha func até eu ver um problema maior nessa organização
        
        return output
