class BuffModel:
    def __init__(self, user, name, priority, path, value, duration):
        import uuid
        self.object_data = { 
            'user': user.combat_profile,
            
            'oid': self.__class__.__name__.lower(),
            'uid': 0,
            'name': name,
        }

        self.buff_data = {
            'origin': None,
            'path': path,
            'address': None,
            'priority_level': priority,
            'update_type': 'default',

            'duration': duration,
            'max_duration': 'default',
            'value': value,

            'can_stack': False,
            'val_stack': None,
            'dur_stack': 3,
            'num_stack': 0,
            
            'conditions': None,
        }

    def get_address(self):
        obj = self.buff_data.get('path')

        if obj is None:
            print(f'{self.object_data['name']}: path not found. Jumping this object in Queue')
            return False
        else:

            from root.attribute_operations import get_attributes

            target  = self.object_data['user']
            attribute = get_attributes(target, obj[0])
            attribute = attribute[obj[1]]
            self.buff_data['address'] = attribute

        return True
    
    def try_apply(self):
        if self.object_data['user'] is None:
            print('No user for this buff. An fatal error are caused')
            return False

        if isinstance(self.buff_data['duration'], int) and self.buff_data['duration'] < 1:
            print(f'{self.object_data['name']} has no duration left.')
            return False
        
        if self.buff_data['value'] <= 0:
            return False

        return True
        
    def conditions(self, target):
        if self.buff_data['conditions'] == None:
            pass
        return True

    def apply(self):
        if self.buff_data['can_stack'] == False:
            self.buff_data['address'][self.buff_data['path'][2]]  += self.buff_data['value']
            print(self.object_data['user'].multipliers['damage']['damage_multiplier'])
        else:
            num = self.buff_data['num_stack']
            self.buff_data['address'][self.buff_data['path'][2]] += self.buff_data['val_stack'][num]
    
    def update(self):
        if self.try_apply():
            if self.get_address() is False:
                return False
        
            self.apply()
            
            if isinstance(self.buff_data['duration'], int):
                self.buff_data['duration'] -= 1
        else:
            return False

        return True

class StackBuffModel(BuffModel):
    def __init__(self, user, name, priority, path, value, duration):
        super().__init__(user, name, priority, path, value, duration)
        self.buff_data['can_stack'] = True
        self.buff_data['dur_stack'] = duration
        self.buff_data['val_stack'] = value
    
    def stack_update(self):
        if self.buff_data['num_stack'] < len(self.buff_data['val_stack']):
            self.buff_data['num_stack'] += 1 

    def update(self):
        if self.get_address() is False:
            return False
        
        if self.try_apply():
            self.apply()
            self.stack_update()

            if isinstance(self.buff_data['duration'], int):
                self.buff_data['duration'] -= 1
        else:
            return False

        return True
    
class DamageBuff(BuffModel):
    def __init__(self, user):
        super().__init__(user, "Damage Buff", 2, ['multipliers', 'damage', 'damage_multiplier'], 0.5, 7)

