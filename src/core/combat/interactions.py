def damage(amount, target, can_miss=False):
    if can_miss:
        import random

        miss_chance = random.uniform(0, 1)
        miss = 0.05

        if miss_chance <= miss:
            return False
        
    current = target.combat_profile.static_stats['hp']['current']
    
    if current - amount < 0:
        current = 0
    else:
        current -= amount
    
    if amount > target.combat_profile.history['damage']['highest']:
        target.combat_profile.history['damage']['highest'] = amount
    target.combat_profile.history['damage']['last_done']   = amount
    target.combat_profile.history['damage']['total']      += amount
    target.combat_profile.history['damage']['last_target'] = target.combat_profile.address

    return True

def heal(amount, target):
    current = target.combat_profile.static_stats['hp']['current'] 
    maximum = target.combat_profile.action_stats['hp']['maximum']
    
    if current + amount > maximum:
        current = maximum
    else:
        current += amount
    
    if amount > target.combat_profile.history['healing']['highest']:
        target.combat_profile.history['healing']['highest'] = amount
    target.combat_profile.history['healing']['last_done']   = amount
    target.combat_profile.history['healing']['total']      += amount
    target.combat_profile.history['healing']['last_target'] = target.combat_profile.address

    return True

def extraheal(amount, target):
    current = target.combat_profile.static_stats['hp']['extra']
    maximum = (target.combat_profile.action_stats['hp']['maximum'] * 1.2)
    
    if current + amount > maximum:
        current = maximum
    else:
        current += amount
    
    return True

def overheal(amount, target):
    current = target.combat_profile.static_stats['hp']['current']
    maximum = target.combat_profile.action_stats['hp']['maximum']
    amount = (amount * target.combat_profile.action_stats['healing']['healing']) + target.combat_profile.multipliers['healing']['healing_bonus']

    if (current + amount) > maximum:
        diff = (current + amount) - maximum
        extraheal(diff, target)
    else:
        current += amount

    return True
          