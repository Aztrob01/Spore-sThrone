def sk_damage(user, target, amount=int, can_miss=False):
    if can_miss:
        import random
        miss = 0.05 + (target.combat_profile.attr.main['dex'] / 100)
        chance = random.uniform(0.01, 1)

        if chance <= miss:
            return False
    
    amount = (amount * user.combat_profile.multipliers['damage']['sk_damage_multiplier']) + user.combat_profile.multipliers['damage']['sk_damage_bonus']
    
    target.combat_profile.static_stats['hp']['current'] -= amount
    user.combat_profile.history['damage']['damage_by_'] += amount
    if amount > user.combat_profile.history['damage']['highest']:
        user.combat_profile.history['damage']['highest'] = amount
    return True

