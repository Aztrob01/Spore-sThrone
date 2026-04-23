import pygame, random, operator

def confirm(user, type, requirements):
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

    signals   = requirements[1]
    operation = operators[signals]

    paths = {
        "base_stats": user.combat_profile.stats.attr.main,
        "stats": user.combat_profile.stats,
        "user": user.combat_profile.user_data,
        "history": user.combat_profile.history,
        "allies": user.combat_stats.allies,
        "targets": user.combat_stats.targets
    }

    if type[0] in paths:
        path = paths[type[0]]

        if len(type) == 3:
            if type[1] in path and type[2] in path[type[1]]:
                longpath = path[type[1]][type[2]]
                if requirements[0] in longpath:
                    return operation(longpath[requirements[0]], requirements[2])
        
        if len(type) == 2:
            if type[1] in path:
                longpath = path[type[1]]
                if requirements[0] in longpath:
                    return operation(longpath[requirements[0]], requirements[2])
    
    return False


            
        
        

    


class Model:
    def __init__(self, name, data, requirements):
        self.requirements = requirements
        self.data = data

    def transfer(self, user, overwrite=False):
        pass

                
    def check(self):
        pass

class Passive(Model):
    def __init__(self, name, requirements):
        passive_data = { 'user': { 'actions': { 'skill': { name: { 'times_used': 0, 'total_cost': 0 } } } } }
        super().__init__(name, passive_data, requirements)

class Pact(Model):
    def __init__(self, name, requirements):
        pact_data = { 'user': { 'actions': { 'pacts': { name: { 'times_activated': 0 } } } } }
        super().__init__(name, pact_data, requirements)

class Active(Model):
    def __init__(self, name, requirements):
        action_data = { 'user': { 'actions': { 'skill': { name: { 'times_used': 0, 'total_cost': 0 } } } } }
        super().__init__(name, action_data, requirements)