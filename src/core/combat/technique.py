import pygame, random, operator
from core.damage import *

def strict_confirm(user, type, requirements):
    """
        strict_confirm check requirements returning a boolean value.
        type = [path, target, subtarget**] that defines the path to the value that will be checked.
        requirepements = [requirement, string_operator, value] that defines requirement to be checked.
        This method isnt cappable of compare requirements, only being used to check if a single requirement is met.
    """
    if len(type) > 3 or len(type) < 2:
        raise ValueError(f'Pathing type(type=) is wrong: {type}')

    operators = {
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne
    }

    paths     = {
        "base_stats": user.combat_profile.stats.attr.main,
        "stats": user.combat_profile.stats,
        "user": user.combat_profile.user_data,
        "history": user.combat_profile.history,
        "allies": user.combat_stats.allies,
        "targets": user.combat_stats.targets
    }

    requirement = requirements[0]
    signal      = operators[requirements[1]]
    value       = requirements[2]

    if type[0] in paths:
        path = paths[type[0]]

        if len(type) == 3:
            if type[1] in path and type[2] in path[type[1]]:
                longpath = path[type[1]][type[2]]
                if requirements[0] in longpath:
                    return signal(longpath[requirement], value)
        
        if len(type) == 2:
            if type[1] in path:
                longpath = path[type[1]]
                if requirements[0] in longpath:
                    return signal(longpath[requirement], value)
    
    return False

def composed_confirm(user, types, requirements):
    pass

class Model:
    def __init__(self, user, name, data, requirements, description):
        self.user = user
        self.description = description
        self.name = name
        self.requirements = requirements
        self.data = data

    def check(self, user):
        for items in self.requirements:
            if items['mode'] == 'simple':
                if not strict_confirm(user, items['type'], items['requirements']):
                    return False
            
            if items['mode'] == 'composed':
                if not composed_confirm(user, items['type'], items['requirements']):
                    return False
                
        return True

    def transfer(self):
        pass

class Passive(Model):
    def __init__(self, user, name, requirements, description):
        passive_data = { 'user': { 'actions': { 'skill': { name: { 'times_used': 0, 'total_cost': 0 } } } } }
        
        super().__init__(user, name, passive_data, requirements, description)

class Pact(Model):
    def __init__(self, user, name, requirements, description):
        pact_data = { 'user': { 'actions': { 'pacts': { name: { 'times_activated': 0 } } } } }
        super().__init__(user, name, pact_data, requirements, description)

class Active(Model):
    def __init__(self, user,  name, requirements, description):
        action_data = { 'user': { 'actions': { 'sk_0': { 'name': name, 'times_used': 0, 'total_cost': 0  } } } }
        super().__init__(user,  name, action_data, requirements, description)


class Vengeance(Active):
    def __init__(self, user):
        requirement = {
        0: {
            'mode': 'simple',
            'type': ['stats', 'mp'],
            'requirements': ['current', '>', 15],
        }
    }
        description = "A powerful strike that grows stronger as the user takes damage. If the target is the last agressor, doubles the damage."
        super().__init__(user, "Vengeance", requirement, description)
        self.data['user']['actions']['sk_0']['highest_damage_dealt'] = 0
        self.data['user']['actions']['sk_0']['highest_damage_taken'] = 0
        self.data['user']['actions']['sk_0']['total_damage_dealt'] = 0
        self.data['user']['actions']['sk_0']['total_damage_taken'] = 0
    
    def use(self, target):
        base_damage = 10 + (self.user.combat_profile.stats.attr.main['str'] / 10) + self.user.combat_profile.history['hp']['lost'] * 0.5
        if self.user.combat_profile.history['resistance']['last_agressor'] == target:
            base_damage *= 2
            self.data['user']['actions']['sk_0']['times_used'] += 1
            self.data['user']['actions']['sk_0']['total_cost'] += 15
        if sk_damage(self.user, target, int(base_damage), True):
            self.data['']