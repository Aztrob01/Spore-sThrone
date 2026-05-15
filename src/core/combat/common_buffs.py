class BuffModel:
    def __init__(self, target, name, priority, duration):
        self.buff_id  = name #!
        self.target   = target
        self.origin   = None
        self.name     = name
        self.type     = None

        self.priority = priority
        self.duration = duration

        self.stats_path  = []
        self.final_path  = None
        self.value       = None


    def check(self):
        if len(self.stats_path) < 3 or self.value is None or self.value == 0:
            print(f'Stats on buff are not correctly defined: p:{self.stats_path} / v:{self.value}')
            return False
        return True

    def conditions(self):
        return False

    def get_path(self):
        
        profile = self.target.combat_profile
        maps = {
            'static': profile.static_stats,
            'multipliers': profile.multipliers,
            'action': profile.action_stats,
            }

        self.final_path = maps[self.stats_path[0]].get(self.stats_path[1])

        return self.final_path != None

    def try_apply(self):
        if self.type is None:
            print(f'{self.name}: Error trying to fetch type {self.type}')
            return False
        if self.buff_id is None:
            print(f'{self.name}: Error trying to fetch id {self.buff_id}')
            return False
        
        path = self.target.combat_profile.status['buffs']

        for objects in path:
            if objects.buff_id == self.buff_id and objects is not self:
                target = objects
                
                if target.type  ==  "UNQ":
                    return False
                elif target.type == "REF":
                    self.duration = target.duration
                    path.remove(target)

        return True                       

    def apply(self):
        stats = self.stats_path[2]
        self.final_path[stats] += self.value
    
    def update(self):
        if self.check() is False:
            return False
        
        if self.final_path == None:
            if self.get_path() is False:
                print(f'{self.name} on {self.target.job.name} has failed to fetch final stats')
                return False
            
        if self.try_apply() is False:
            return False
        
        if isinstance(self.duration, int):
            if self.duration > 0:
                self.duration -= 1
            else:
                return False

        self.apply()

        return True
    
class StackBuffModel(BuffModel):
    def __init__(self, target, name, priority, duration, type, stacks, stack_duration):
        super().__init__(target, name, priority, duration, type)
        self.stack = stacks
        self.stack_duration = stack_duration
        self.stack_position = 0
        
        self.stack_length   = (len(self.stack) - 1)
