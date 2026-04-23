from core.combat.technique import *
from core.damage import *
import random

class Ac1(Technique):
    def __init__(self):
        super().__init__("Direct Attack", Active(), [("user", "mp", ">", 15)], None)
        self.typeoftarget, self.typeofarea, self.targetrange  = (['enemy'], 'single')
        self.base_damage = 10

    def use(self, user, target):
        damage     = ((self.base_damage + (user.combat_profile.attr.main['str'] / 2) + (0.1 * user.combat_profile.stats['level']['current'])) * user.combat_profile.stats['damage']['ab_damage_multiplier'])
        resistance = (target.combat_profile.attr.main['res'] * target.combat_profile.stats['resistance']['ab_resistance_multiplier'])
        damage     = damage - resistance

        sk_damage(user, target, damage, True)

class Pa1(Technique):
    def __init__(self):
        super().__init__("Counter Attack!", Passive(), [("user", "get_hitted", "==", True)], None)
        
    def use(self, user, target):
        pass

  