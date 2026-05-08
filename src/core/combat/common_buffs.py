class BuffModel:
    def __init__(self, name, priority, duration):
        self.type            = 'buff'
        self.name            = name 
        self.duration        = duration
        self.priority        = priority

        self.stats_path  = []
        self.final_path  = None
        self.value       = None

    def check(self):
        if len(self.stats_path) < 3:
            raise ValueError(f'Stats on buff are not correctly defined: {self.stats_path}')
        if self.value is None or self.value == 0:
            raise ValueError(f'{self.name} cannot be loaded. inner value error.')
        return True

    def get_path(self, target):
        profile = target.combat_profile
        maps = {
            'static': target.combat_profile.static_stats,
            'multipliers': target.combat_profile.multipliers,
            'action': target.combat_profile.action_stats,
        }

        self.final_path = maps[self.stats_path[0]].get(self.stats_path[1])

    def apply(self, target):
        stats = self.stats_path[2]
        self.final_path[stats] += self.value
    
    def update(self, target):
        self.check()
        if self.final_path == None:
            self.get_path(target)
        self.apply(target)
        
        if isinstance(self.duration, int):
            self.duration -= 1
        
        return True
    
class StackableBuff(BuffModel):
    def __init__(self, name, priority, duration, stack_duration, stacks):
        super().__init__(name, priority, duration)
        self.stack_duration = stack_duration


class HealingAuraBuff(BuffModel):
    def __init__(self, priority=8, duration=4):
        super().__init__("Healing Aura", priority, duration)
        self.stats_path  = ['static', 'hp', 'current']
        self.value = 15
    
    def apply(self, target):
        stats = self.stats_path[2]
        multipliers = target.combat_profile.multipliers['healing']
        self.final_path[stats] += (self.value * multipliers['healing_multiplier']) + multipliers['healing_bonus']

    